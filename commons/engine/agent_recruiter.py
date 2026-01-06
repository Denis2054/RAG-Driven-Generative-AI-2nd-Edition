# agent_recruiter.py
# Copyright 2026, Denis Rothman
# The Oracle Recruiter (Hybrid Retriever)
# -------------------------------------------------------------------------
# This agent acts as a Domain Specialist in the Universal Context Engine.
# Unlike the Archivist (which just finds text), this agent understands
# Structured Business Logic.
#
# ROLE:
# It performs Hybrid RAG:
# 1. Semantic Search (Vector) for skills/bio match.
# 2. SQL Filtering (Scalar) for salary and experience constraints.
#
# INPUT (MCP Message Content):
# {
#   "intent_query": "Find a Python Team Lead",
#   "constraints": {
#       "max_salary": 160000,
#       "min_experience": 5
#   }
# }
#
# OUTPUT (MCP Message Content):
# {
#   "candidates": [
#       {"name": "Quinn", "score": 0.89, "salary": 155000, "summary": "..."},
#       ...
#   ]
# }
# -------------------------------------------------------------------------

import logging
import oracledb
import json
from helpers import create_mcp_message
from oracle_lib import OracleManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [Recruiter] - %(levelname)s - %(message)s')

def agent_oracle_recruiter(mcp_message, client, embedding_model="text-embedding-3-small"):
    """
    Retrieves candidates from Oracle 23ai's CANDIDATE_POOL using Hybrid Search.
    """
    agent_name = "OracleRecruiter"
    logging.info(f"[{agent_name}] Activated.")

    try:
        # 1. Parse Input
        content = mcp_message.get('content', {})
        user_query = content.get('intent_query')
        constraints = content.get('constraints', {})
        
        # Default constraints if not provided
        max_salary = constraints.get('max_salary', 1000000)
        min_experience = constraints.get('min_experience', 0)

        if not user_query:
            raise ValueError(f"[{agent_name}] Input requires 'intent_query'.")

        logging.info(f"[{agent_name}] Searching: '{user_query}' (Sal <= {max_salary}, Exp >= {min_experience})")

        # 2. Vectorize the Query
        response = client.embeddings.create(input=user_query, model=embedding_model)
        query_vector = response.data[0].embedding

        # 3. Execute Hybrid SQL on Oracle
        candidates_found = []
        
        with OracleManager.get_cursor() as cursor:
            # The Hybrid Query from Chapter 3
            # Filters by SQL (WHERE) and Ranks by VECTOR (ORDER BY)
            sql = """
                SELECT candidate_id, full_name, years_experience, salary_expectation, summary,
                       VECTOR_DISTANCE(resume_vector, :v, DOT) as similarity
                FROM candidate_pool
                WHERE salary_expectation <= :max_sal
                  AND years_experience >= :min_exp
                ORDER BY similarity DESC
                FETCH FIRST 3 ROWS ONLY
            """
            
            # Explicitly tell the driver this input is a vector
            cursor.setinputsizes(v=oracledb.DB_TYPE_VECTOR)
            
            cursor.execute(sql, {
                "v": query_vector,
                "max_sal": max_salary,
                "min_exp": min_experience
            })
            
            rows = cursor.fetchall()
            
            for row in rows:
                c_id, name, exp, sal, summary_lob, score = row
                
                # Handle CLOB conversion safely
                summary_text = summary_lob.read() if hasattr(summary_lob, 'read') else str(summary_lob)
                
                logging.info(f"[{agent_name}] Match: {name} (Score: {score:.3f}, Sal: {sal})")
                
                candidates_found.append({
                    "id": c_id,
                    "name": name,
                    "experience": exp,
                    "salary": sal,
                    "match_score": float(score), # Ensure JSON serializable
                    "summary": summary_text
                })

        # 4. Format Output (MCP Standard)
        # We return a structured list, but also a text block for the Writer to use easily
        formatted_text_block = ""
        for c in candidates_found:
            formatted_text_block += (
                f"--- CANDIDATE: {c['name']} (ID: {c['id']}) ---\n"
                f"Score: {c['match_score']:.3f}\n"
                f"Experience: {c['experience']} years\n"
                f"Salary: ${c['salary']:,}\n"
                f"Summary: {c['summary']}\n\n"
            )

        output_content = {
            "candidate_list": candidates_found,
            "retrieved_context": formatted_text_block, # Standard key for Writer compatibility
            "source": "Oracle 23ai (Hybrid Search)"
        }
        
        return create_mcp_message(agent_name, output_content)

    except Exception as e:
        logging.error(f"[{agent_name}] Failed: {e}")
        return create_mcp_message(agent_name, {"error": str(e)})
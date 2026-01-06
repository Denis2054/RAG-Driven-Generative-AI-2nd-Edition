# agent_archivist.py
# Copyright 2026, Denis Rothman
# The Oracle Archivist (Unstructured Retriever)
# -------------------------------------------------------------------------
# This agent is the functional equivalent of the "Researcher" in Chapter 5,
# but it speaks to Oracle 23ai instead of Pinecone.
#
# ROLE:
# It retrieves unstructured knowledge (text chunks) from the KNOWLEDGE_STORE
# table based on semantic similarity.
#
# INPUT (MCP Message Content):
# {
#   "intent_query": "What happened during the cyber incident?"
# }
#
# OUTPUT (MCP Message Content):
# {
#   "retrieved_context": "Server logs indicate unauthorized access at 03:00..."
# }
# -------------------------------------------------------------------------

import logging
import oracledb
from helpers import create_mcp_message
from oracle_lib import OracleManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [Archivist] - %(levelname)s - %(message)s')

def agent_oracle_archivist(mcp_message, client, embedding_model="text-embedding-3-small"):
    """
    Retrieves unstructured text from Oracle 23ai's KNOWLEDGE_STORE table.
    """
    agent_name = "OracleArchivist"
    logging.info(f"[{agent_name}] Activated.")

    try:
        # 1. Parse Input
        content = mcp_message.get('content', {})
        user_query = content.get('intent_query') or content.get('topic_query')
        
        if not user_query:
            raise ValueError(f"[{agent_name}] Input requires 'intent_query' or 'topic_query'.")

        logging.info(f"[{agent_name}] Processing query: '{user_query}'")

        # 2. Vectorize the Query
        # We reuse the client passed from the Engine (Chapter 5 style)
        response = client.embeddings.create(input=user_query, model=embedding_model)
        query_vector = response.data[0].embedding

        # 3. Execute Vector Search on Oracle
        # We use the OracleManager singleton to get a cursor
        retrieved_text_blocks = []
        
        with OracleManager.get_cursor() as cursor:
            # Note: We use the DOT product metric, consistent with Chapter 2
            sql = """
                SELECT text, VECTOR_DISTANCE(embedding, :v, DOT) as score
                FROM knowledge_store
                ORDER BY score DESC
                FETCH FIRST 3 ROWS ONLY
            """
            
            # Explicitly tell the driver this input is a vector
            cursor.setinputsizes(v=oracledb.DB_TYPE_VECTOR)
            cursor.execute(sql, {"v": query_vector})
            
            rows = cursor.fetchall()
            
            for row in rows:
                text_chunk = row[0].read() if hasattr(row[0], 'read') else str(row[0])
                score = row[1]
                logging.info(f"[{agent_name}] Found match (Score: {score:.3f})")
                retrieved_text_blocks.append(text_chunk)

        if not retrieved_text_blocks:
            logging.warning(f"[{agent_name}] No relevant documents found.")
            combined_context = "No relevant documents found in the Knowledge Store."
        else:
            combined_context = "\n\n--- DOCUMENT EVIDENCE ---\n".join(retrieved_text_blocks)

        # 4. Format Output (MCP Standard)
        output_content = {
            "retrieved_context": combined_context,
            "source": "Oracle 23ai (KNOWLEDGE_STORE)"
        }
        
        return create_mcp_message(agent_name, output_content)

    except Exception as e:
        logging.error(f"[{agent_name}] Failed: {e}")
        # Return a safe error message instead of crashing the whole engine
        return create_mcp_message(agent_name, {"error": str(e)})
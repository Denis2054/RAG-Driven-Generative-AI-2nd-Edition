# FILE: registry.py (Chapter 5 Integration)
# Copyright 2026, Denis Rothman

# === Imports ===
import logging
import agents  # The original Pinecone agents (Standard)
# Import the NEW Oracle agents (Enterprise)
import agent_archivist 
import agent_recruiter
from helpers import create_mcp_message

# === 5. The Agent Registry (Universal Edition) ===
class AgentRegistry:
    def __init__(self):
        self.registry = {
            # --- Standard Pinecone Agents (Original) ---
            "Librarian": agents.agent_context_librarian,
            "Researcher": agents.agent_researcher,
            "Writer": agents.agent_writer,
            "Summarizer": agents.agent_summarizer,
            
            # --- New Oracle Enterprise Agents (Chapter 4) ---
            "OracleArchivist": agent_archivist.agent_oracle_archivist,
            "OracleRecruiter": agent_recruiter.agent_oracle_recruiter,
        }

    def get_handler(self, agent_name, client, index, generation_model, embedding_model, namespace_context, namespace_knowledge):
        """
        Retrieves the appropriate agent function and curries it with the necessary infrastructure clients.
        """
        handler_func = self.registry.get(agent_name)
        if not handler_func:
            logging.error(f"Agent '{agent_name}' not found in registry.")
            raise ValueError(f"Agent '{agent_name}' not found in registry.")

        # --- Handler Mapping Logic ---
        
        # 1. Librarian (Pinecone Context)
        if agent_name == "Librarian":
            return lambda mcp_message: handler_func(
                mcp_message, 
                client=client, 
                index=index, 
                embedding_model=embedding_model, 
                namespace_context=namespace_context
            )
            
        # 2. Researcher (Pinecone Knowledge)
        elif agent_name == "Researcher":
            return lambda mcp_message: handler_func(
                mcp_message, 
                client=client, 
                index=index, 
                generation_model=generation_model, 
                embedding_model=embedding_model, 
                namespace_knowledge=namespace_knowledge
            )
            
        # 3. Writer & Summarizer (LLM Only)
        elif agent_name == "Writer" or agent_name == "Summarizer":
            return lambda mcp_message: handler_func(
                mcp_message, 
                client=client, 
                generation_model=generation_model
            )
            
        # 4. OracleArchivist (Oracle Knowledge Store)
        elif agent_name == "OracleArchivist":
            return lambda mcp_message: handler_func(
                mcp_message, 
                client=client, 
                embedding_model=embedding_model
            )
            
        # 5. OracleRecruiter (Oracle Candidate Pool)
        elif agent_name == "OracleRecruiter":
            return lambda mcp_message: handler_func(
                mcp_message, 
                client=client, 
                embedding_model=embedding_model
            )

        else:
            raise ValueError(f"Configuration missing for agent: {agent_name}")

    def get_capabilities_description(self):
        """
        Returns a detailed description of available agents and their inputs.
        Used by the Planner (LLM) to generate execution plans.
        """
        return """
AVAILABLE CAPABILITIES:
-----------------------
1. Librarian
   - Role: Retrieves style/structure blueprints (templates).
   - Input: {"intent_query": "string description of the desired content style"}

2. Researcher
   - Role: Searches for factual information in the Pinecone Knowledge Base.
   - Input: {"topic_query": "string topic to research"}

3. Writer
   - Role: Generates final content by applying a Blueprint to Facts.
   - Input: {"blueprint": "string context", "facts": "string evidence", "previous_content": "optional string"}

4. Summarizer
   - Role: Reduces large text blocks to concise summaries.
   - Input: {"text_to_summarize": "string", "summary_objective": "string goal"}

5. OracleArchivist
   - Role: Retrieves unstructured documents (logs, reports) from the Oracle Database.
   - Input: {"intent_query": "string search query"}

6. OracleRecruiter
   - Role: Retrieves job candidates from Oracle Database using Hybrid Search (Structured + Semantic).
   - Input: {
       "intent_query": "string (e.g., 'Python Developer')", 
       "constraints": {"max_salary": integer, "min_experience": integer}
     }
"""

    def list_agents(self):
        """Alias for capabilities description, useful for UI display."""
        return self.get_capabilities_description()

# Initialize the global toolkit.
AGENT_TOOLKIT = AgentRegistry()
logging.info("Agent Registry initialized with Universal capabilities (Pinecone + Oracle).")
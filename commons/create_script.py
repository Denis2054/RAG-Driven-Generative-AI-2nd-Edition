"""
Schema Registry for Oracle DBA Console
This file acts as a catalog for Data Definition Language (DDL) statements.
It is fetched dynamically by the notebook to ensure the latest schema definitions are used.
"""

DDL_CATALOG = {
    "CHAPTER_2": [
        {
            "table_name": "CONTEXT_LIBRARY",
            "description": "Stores structured blueprints and metadata for RAG retrieval.",
            "sql": """
            CREATE TABLE context_library (
                id VARCHAR2(200) PRIMARY KEY,
                description CLOB,
                blueprint_json CLOB,
                embedding VECTOR(1536)
            )
            """
        },
        {
            "table_name": "KNOWLEDGE_STORE",
            "description": "Stores unstructured text chunks linked to vector embeddings.",
            "sql": """
            CREATE TABLE knowledge_store (
                id VARCHAR2(200) PRIMARY KEY,
                source VARCHAR2(200),
                text CLOB,
                embedding VECTOR(1536)
            )
            """
        }
    ],
    "CHAPTER_3": [
        {
            "table_name": "CANDIDATE_POOL",
            "description": "Hybrid table mixing SQL structured data (Salary, Exp) with Vectors.",
            "sql": """
            CREATE TABLE candidate_pool (
                candidate_id VARCHAR2(50) PRIMARY KEY,
                full_name VARCHAR2(100),
                summary CLOB,
                skills VARCHAR2(1000),
                years_experience NUMBER,
                salary_expectation NUMBER,
                resume_vector VECTOR(1536)
            )
            """
        },
        {
            "table_name": "RECRUITMENT_RULES",
            "description": "Stores Agent Personas and domain-specific evaluation criteria.",
            "sql": """
            CREATE TABLE recruitment_rules (
                rule_id VARCHAR2(50) PRIMARY KEY,
                agent_persona CLOB,
                evaluation_criteria CLOB,
                rule_vector VECTOR(1536)
            )
            """
        }
    ]
}

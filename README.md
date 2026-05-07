# RAG-Driven Generative AI, Second Edition

## Build MAS-RAG with DualRAG, GraphRAG, and multimodal video pipelines on Oracle AI Database 26ai (database engine: Oracle Database 23ai)

  
Copyright 2025-2026, Denis Rothman.  

**Last updated: May 6, 2026**

See the [Changelog](https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/CHANGELOG.md) for updates, fixes, and upgrades (past, present, coming).


## Bringing AI to the data

The era of extracting sensitive enterprise data to external AI platforms is under fire. This second edition defines a revolutionary architectural shift: **bringing the AI to the data**. This repository shows you how to build Sovereign AI systems that keep your most critical assets secure and governed within Oracle's converged engine, eliminating the fragmentation, latency, and security risks inherent in traditional data extraction. *The repository implements Oracle AI Database 26ai, powered by the Oracle Database 23ai engine, and opens the door to other AI‑to‑data databases such as SQL Server or any database you are integrating.*

<a href="https://www.packtpub.com/en-us/product/rag-driven-generative-ai-9781836200901">
  <img src="https://camo.githubusercontent.com/e531a423a74f926309487643292f34ac5314e8d2fb78371cfce182d5a1ff340c/68747470733a2f2f636f6e74656e742e7061636b742e636f6d2f4233373731342f636f7665725f696d6167655f736d616c6c2e6a7067" alt="RAG-Driven Generative AI, Second Edition" align="left" width="220" hspace="20" vspace="10">
</a>



**Dual RAG** is the definitive methodology for defeating hallucinations and data poisoning simultaneously. By synchronizing unstructured vector semantics with the deterministic truth of structured SQL, Graph, and Spatial retrieval, your agents reason over verified corporate facts rather than probabilistic guesses. From there, you will move beyond simple pipelines to master **MAS-RAG** (multi-agent systems for RAG): a **Universal Context Engine** with a Planner, an Agent Registry, and sovereign Oracle agents coordinating across hybrid retrieval workflows, Hybrid Adaptive RAG feedback loops, and multimodal video pipelines.

You will engineer a single converged hyper-query that fuses vector similarity, Oracle Spatial (SDO_GEOMETRY), and SQL Property Graphs (SQL/PGQ) without data movement, scale MAS-RAG workloads to millions of vectors using Oracle Exadata AI Smart Scan, and culminate by deploying an **Autonomous Database Architect** — an agent that constructs its own governed relational structures. 
<br clear="left">


## Key Learnings

* **Sovereign AI architecture:** bring intelligence directly to the data within Oracle Database 23ai, eliminating data extraction risk
* **Dual Path RAG:** synchronise unstructured vector semantics with deterministic structured SQL to defeat hallucinations and data poisoning simultaneously
* **MAS-RAG pipelines:** build a Universal Context Engine with Planner, Agent Registry, and MCP-standardised sovereign agents that replace external vector databases
* **Hybrid Adaptive RAG:** engineer a dynamic inference-time router that switches between model reasoning, RAG retrieval, and expert human feedback injection based on cosine similarity scores and user rankings
* **Converged hyper-query:** fuse vector similarity, Oracle Spatial (SDO_GEOMETRY), and SQL Property Graph (SQL/PGQ) traversal in a single execution context with zero data movement
* **Multimodal video RAG:** build a pipeline with a version-controlled Schema Registry, RLHF-curated metadata, and semantic vector search over segmented visual assets
* **RAGOps at scale:** leverage Oracle Exadata AI Smart Scan to eliminate the data movement tax on high-dimensional vector distance calculations
* **Autonomous Database Architect:** deploy an agent on a Perceive–Plan–Act–Audit loop, capable of generating Oracle DDL and orchestrating ETL Workers from raw unstructured enterprise data

## Chapters

| Chapters | Colab | Kaggle | Studio Lab |
| --- | --- | --- | --- |
| **Chapter 1: Why Retrieval-Augmented Generation?** |  |  |  |
| <ul><li>RAG_Overview_db.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter01/RAG_Overview_db.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter01/RAG_Overview_db.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter01/RAG_Overview_db.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 2: RAG Embeddings in Oracle Vector Stores** |  |  |  |
| <ul><li>1_DBA_Oracle_Management.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/1_DBA_Oracle_Management.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/1_DBA_Oracle_Management.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/1_DBA_Oracle_Management.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| <ul><li>2_Oracle_Data_Acquisition.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/2_Oracle_Data_Acquisition.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/2_Oracle_Data_Acquisition.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/2_Oracle_Data_Acquisition.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| <ul><li>3_LLM_Augmented_Query.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/3_LLM_Augmented_Query.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/3_LLM_Augmented_Query.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/3_LLM_Augmented_Query.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 3: Building a Live Recruiter Agent** |  |  |  |
| <ul><li>1_DBA_Oracle_Management_V2.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/1_DBA_Oracle_Management_V2.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/1_DBA_Oracle_Management_V2.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/1_DBA_Oracle_Management_V2.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| <ul><li>2_Data_Ingestion_Oracle_DB.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/2_Data_Ingestion_Oracle_DB.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/2_Data_Ingestion_Oracle_DB.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/2_Data_Ingestion_Oracle_DB.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| <ul><li>3_LLM_Augmented_Hybrid_Query.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/3_LLM_Augmented_Hybrid_Query.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/3_LLM_Augmented_Hybrid_Query.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/3_LLM_Augmented_Hybrid_Query.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 4: Building Sovereign Enterprise Agents** |  |  |  |
| <ul><li>Unified_Agents_Unit_Test.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter04/Unified_Agents_Unit_Test.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter04/Unified_Agents_Unit_Test.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter04/Unified_Agents_Unit_Test.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 5: Building a Universal Context Engine** |  |  |  |
| <ul><li>Universal_Context_Engine_Converged_Edition.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter05/Universal_Context_Engine_Converged_Edition.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter05/Universal_Context_Engine_Converged_Edition.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter05/Universal_Context_Engine_Converged_Edition.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 6: Operationalizing the Universal Context Engine** |  |  |  |
| <ul><li>Universal_Context_Engine_UI_Oracle.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter06/Universal_Context_Engine_UI_Oracle.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter06/Universal_Context_Engine_UI_Oracle.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter06/Universal_Context_Engine_UI_Oracle.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 7: Empowering AI Models by Fine-Tuning RAG Data** |  |  |  |
| <ul><li>Fine_tuning_OpenAI_GPT_4o_mini.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter07/Fine_tuning_OpenAI_GPT_4o_mini.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter07/Fine_tuning_OpenAI_GPT_4o_mini.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter07/Fine_tuning_OpenAI_GPT_4o_mini.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 8: Boosting RAG Performance with Human Feedback** |  |  |  |
| <ul><li>Adaptive_RAG.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter08/Adaptive_RAG.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter08/Adaptive_RAG.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter08/Adaptive_RAG.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 9: Building a Conversational RAG Agent** |  |  |  |
| <ul><li>Conversational_RAG_Video_Store_Agent.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Conversational_RAG_Video_Store_Agent.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Conversational_RAG_Video_Store_Agent.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Conversational_RAG_Video_Store_Agent.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| <ul><li>Video_dataset_visualization.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Video_dataset_visualization.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Video_dataset_visualization.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Video_dataset_visualization.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 10: Building an Agent with Spatial-RAG and GraphRAG** |  |  |  |
| <ul><li>Oracle_Spatial_Graph.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter10/Oracle_Spatial_Graph.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter10/Oracle_Spatial_Graph.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter10/Oracle_Spatial_Graph.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 11: Scaling AI Workloads with Oracle Exadata** |  |  |  |
| <ul><li>Scaling_AI_Workloads_Oracle_Exadata.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter11/Scaling_AI_Workloads_Oracle_Exadata.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter11/Scaling_AI_Workloads_Oracle_Exadata.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter11/Scaling_AI_Workloads_Oracle_Exadata.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **Chapter 12: The Autonomous Database Architect** |  |  |  |
| <ul><li>The_Autonomous_Database_Architect.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter12/The_Autonomous_Database_Architect.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter12/The_Autonomous_Database_Architect.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter12/The_Autonomous_Database_Architect.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
| **The Oracle DBA Console** |  |  |  |
| <ul><li>Oracle_DBA_Console.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/commons/Oracle_DBA_Console.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/commons/Oracle_DBA_Console.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/commons/Oracle_DBA_Console.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a> |
The Oracle DBA Console serves as the Control Center for the Oracle Database 23ai (Oracle AI Database 26ai) Hybrid Vector Database of the entire GitHub repository.
[![](https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/raw/main/commons/architecture_dba.png)](https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/raw/main/commons/architecture_dba.png)

## Requirements for this book

## Technical Requirements

To get the most out of this book, ensure you have the following background and setup:

### Knowledge Requirements

* Proficiency in **Python**
* Working knowledge of **SQL** and **REST APIs**
* Foundational understanding of **LLM orchestration**
* Ability to navigate **cloud consoles**
* Comfort with **notebook-based workflows** for implementing multi-agent systems

### Software & Platform Requirements

* Access to a **Google Colab** environment
* An **Oracle Cloud Free Tier** account to provision an **Autonomous Database 23ai** instance (provisioned through the Oracle AI Database 26ai console)
* An **OpenAI API key** for powering reasoning engines and fine-tuning pipelines

### Hardware Requirements

* A system capable of running a modern web browser smoothly
* Stable internet connection for cloud-based development and API usage



## Get to know the Author

*Denis Rothman* has been designing and deploying AI systems for more than three decades.
After graduating from Sorbonne University and Paris Cité University, he taught at Panthéon
Sorbonne University, where he registered an early patent for word tokenization and encoding,
followed by a patent for a conversational human–machine system. Since then, he has created
pioneering AI applications ranging from cognitive NLP chatbots for language learning to
aerospace AI solutions, global supply chain optimizers, and advanced planning and scheduling
systems used worldwide.  
An early advocate of explainable AI, Denis has consistently built interpretable interfaces and
explanation data into complex projects across aerospace, apparel, and automotive industries.
His belief that knowledge is only complete when it is shared has led him to author multiple
books on AI, distilling his hands-on expertise into algorithms, frameworks, and platforms.
Model- and platform-agnostic, Denis combines theory with pragmatic, full-stack
development, providing not just concepts but also working code that readers can experiment
with and build upon.




## Other Related Books

* [Context Engineering for Multi-Agent Systems, First Edition](https://www.amazon.com/dp/1806690055)
* [Building Business‑Ready Generative AI Systems](https://www.amazon.com/dp/B0FDQJRB7Q)

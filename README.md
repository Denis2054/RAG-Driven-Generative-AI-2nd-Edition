# RAG-Driven Generative AI, Second Edition</h1>

<h2 align="left">
Build MAS-RAG with DualRAG, GraphRAG,<br>
multimodal video pipelines, and Oracle Database 23ai
</h2>

<br clear="left"/>
<p align="left">Copyright 2025-2026, Denis Rothman. <strong>Last updated: April 9, 2026</strong></p>
<p align="left">See the <a href="./CHANGELOG.md">Changelog</a> for updates, fixes, and upgrades(past, present, coming).</p>

<p align="left">
   <a href="https://packt.link/I1tSU" alt="Discord" title="Learn more on the Discord server"><img width="32px" src="https://cliply.co/wp-content/uploads/2021/08/372108630_DISCORD_LOGO_400.gif"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
<!--   <a href="https://packt.link/free-ebook/9781807424954"><img width="32px" alt="Free PDF" title="Free PDF with purchased book" src="https://cdn-icons-png.flaticon.com/512/4726/4726010.png"/></a>
 &#8287;&#8287;&#8287;&#8287;&#8287;
<a href="https://packt.link/gbp/9781807424954"><img width="32px" alt="Graphic Bundle" title="Graphic Bundle" src="https://cdn-icons-png.flaticon.com/512/2659/2659360.png"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
<a href="https://www.amazon.com/RAG-Driven-Generative-retrieval-generation-LlamaIndex/dp/1836200919/ref=tmm_pap_swatch_0"><img width="32px" alt="Amazon" title="Get your copy" src="https://cdn-icons-png.flaticon.com/512/15466/15466027.png"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;</p> -->
</p>
<details open>
  <summary><h2>About the book(coming by end of April 2026, stay tuned!) </h2></summary>
<a href="https://www.packtpub.com/en-us/product/rag-driven-generative-ai-9781836200901">
<img src="https://content.packt.com/B37714/cover_image_small.jpg" alt="RAG-Driven Generative AI, Second Edition" height="256px" align="right">
</a>

The era of extracting sensitive enterprise data to external AI platforms is under fire. This second edition defines a **revolutionary architectural shift that brings AI to the data.** The book shows you how to build Sovereign AI systems that keep your most critical assets secure and governed within Oracle Database 23ai's converged engine, eliminating the fragmentation, latency, and security risks inherent in traditional data extraction.

At the core of this edition is **Dual RAG**, the definitive methodology for defeating hallucinations and data poisoning simultaneously. By synchronizing unstructured vector semantics with the deterministic truth of structured SQL, Graph, and Spatial retrieval, your agents reason over verified corporate facts rather than probabilistic guesses. From there, you will move beyond simple pipelines to master **MAS-RAG** (multi-agent systems for RAG): a Universal Context Engine with a Planner, an Agent Registry, and sovereign Oracle agents coordinating across hybrid retrieval workflows, Hybrid Adaptive RAG feedback loops, and multimodal video pipelines.

The final arc of the book transcends retrieval entirely. You will engineer a single converged hyper-query that fuses vector similarity, Oracle Spatial (SDO_GEOMETRY), and SQL Property Graphs (SQL/PGQ) without data movement, scale MAS-RAG workloads to millions of vectors using Oracle Exadata AI Smart Scan, and culminate by deploying an Autonomous Database Architect — an agent that perceives raw enterprise chaos and constructs its own governed relational structures on a Perceive–Plan–Act–Audit loop.

Designed for enterprise AI architects and senior developers proficient in Python and LLM orchestration, this is an advanced architectural deep-dive with battle-tested blueprints for every stage of the Sovereign AI lifecycle.

</details>

<details open>
  <summary><h2>Key Learnings</h2></summary>
<ul>
<li><b>Sovereign AI architecture:</b> bring intelligence directly to the data within Oracle Database 23ai, eliminating data extraction risk</li>
<li><b>Dual Path RAG:</b> synchronise unstructured vector semantics with deterministic structured SQL to defeat hallucinations and data poisoning simultaneously</li>
<li><b>MAS-RAG pipelines:</b> build a Universal Context Engine with Planner, Agent Registry, and MCP-standardised sovereign agents that replace external vector databases</li>
<li><b>Hybrid Adaptive RAG:</b> engineer a dynamic inference-time router that switches between model reasoning, RAG retrieval, and expert human feedback injection based on cosine similarity scores and user rankings</li>
<li><b>Converged hyper-query:</b> fuse vector similarity, Oracle Spatial (SDO_GEOMETRY), and SQL Property Graph (SQL/PGQ) traversal in a single execution context with zero data movement</li>
<li><b>Multimodal video RAG:</b> build a pipeline with a version-controlled Schema Registry, RLHF-curated metadata, and semantic vector search over segmented visual assets</li>
<li><b>RAGOps at scale:</b> leverage Oracle Exadata AI Smart Scan to eliminate the data movement tax on high-dimensional vector distance calculations</li>
<li><b>Autonomous Database Architect:</b> deploy an agent on a Perceive–Plan–Act–Audit loop, capable of generating Oracle DDL and orchestrating ETL Workers from raw unstructured enterprise data</li>
</ul>
</details>

<details open>
<summary><h2>Chapters</h2></summary>


| Chapters | Colab | Kaggle | Studio Lab |
| :-------- | :-------- | :-------- | :-------- |
| **Chapter 1: Why Retrieval-Augmented Generation?** | | | |
| <ul><li>RAG_Overview_db.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter01/RAG_Overview_db.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter01/RAG_Overview_db.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter01/RAG_Overview_db.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 2: RAG Embeddings in Oracle Vector Stores** | | | |
| <ul><li>1_DBA_Oracle_Management.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/1_DBA_Oracle_Management.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/1_DBA_Oracle_Management.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/1_DBA_Oracle_Management.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| <ul><li>2_Oracle_Data_Acquisition.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/2_Oracle_Data_Acquisition.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/2_Oracle_Data_Acquisition.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/2_Oracle_Data_Acquisition.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| <ul><li>3_LLM_Augmented_Query.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/3_LLM_Augmented_Query.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/3_LLM_Augmented_Query.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter02/3_LLM_Augmented_Query.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 3: Building a Live Recruiter Agent** | | | |
| <ul><li>1_DBA_Oracle_Management_V2.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/1_DBA_Oracle_Management_V2.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/1_DBA_Oracle_Management_V2.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/1_DBA_Oracle_Management_V2.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| <ul><li>2_Data_Ingestion_Oracle_DB.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/2_Data_Ingestion_Oracle_DB.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/2_Data_Ingestion_Oracle_DB.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/2_Data_Ingestion_Oracle_DB.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| <ul><li>3_LLM_Augmented_Hybrid_Query.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/3_LLM_Augmented_Hybrid_Query.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/3_LLM_Augmented_Hybrid_Query.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter03/3_LLM_Augmented_Hybrid_Query.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 4: Building Sovereign Enterprise Agents** | | | |
| <ul><li>Unified_Agents_Unit_Test.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter04/Unified_Agents_Unit_Test.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter04/Unified_Agents_Unit_Test.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter04/Unified_Agents_Unit_Test.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 5: Building a Universal Context Engine** | | | |
| <ul><li>Universal_Context_Engine_Converged_Edition.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter05/Universal_Context_Engine_Converged_Edition.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter05/Universal_Context_Engine_Converged_Edition.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter05/Universal_Context_Engine_Converged_Edition.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 6: Operationalizing the Universal Context Engine** | | | |
| <ul><li>Universal_Context_Engine_UI_Oracle.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter06/Universal_Context_Engine_UI_Oracle.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter06/Universal_Context_Engine_UI_Oracle.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter06/Universal_Context_Engine_UI_Oracle.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 7: Empowering AI Models by Fine-Tuning RAG Data** | | | |
| <ul><li>Fine_tuning_OpenAI_GPT_4o_mini.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter07/Fine_tuning_OpenAI_GPT_4o_mini.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter07/Fine_tuning_OpenAI_GPT_4o_mini.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter07/Fine_tuning_OpenAI_GPT_4o_mini.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 8: Boosting RAG Performance with Human Feedback** | | | |
| <ul><li>Adaptive_RAG.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter08/Adaptive_RAG.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter08/Adaptive_RAG.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter08/Adaptive_RAG.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 9: Building a Conversational RAG Agent** | | | |
| <ul><li>Conversational_RAG_Video_Store_Agent.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Conversational_RAG_Video_Store_Agent.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Conversational_RAG_Video_Store_Agent.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Conversational_RAG_Video_Store_Agent.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| <ul><li>Video_dataset_visualization.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Video_dataset_visualization.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Video_dataset_visualization.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter09/Video_dataset_visualization.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 10: Building an Agent with Spatial-RAG and GraphRAG** | | | |
| <ul><li>Oracle_Spatial_Graph.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter10/Oracle_Spatial_Graph.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter10/Oracle_Spatial_Graph.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter10/Oracle_Spatial_Graph.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 11: Scaling AI Workloads with Oracle Exadata** | | | |
| <ul><li>Scaling_AI_Workloads_Oracle_Exadata.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter11/Scaling_AI_Workloads_Oracle_Exadata.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter11/Scaling_AI_Workloads_Oracle_Exadata.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter11/Scaling_AI_Workloads_Oracle_Exadata.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **Chapter 12: The Autonomous Database Architect** | | | |
| <ul><li>The_Autonomous_Database_Architect.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter12/The_Autonomous_Database_Architect.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter12/The_Autonomous_Database_Architect.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/Chapter12/The_Autonomous_Database_Architect.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |
| **The Oracle DBA Console** | | | |
| <ul><li>Oracle_DBA_Console.ipynb</li></ul> | <a href="https://colab.research.google.com/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/commons/Oracle_DBA_Console.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a><br> | <a href="https://www.kaggle.com/kernels/welcome?src=https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/commons/Oracle_DBA_Console.ipynb"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a><br> | <a href="https://studiolab.sagemaker.aws/import/github/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/blob/main/commons/Oracle_DBA_Console.ipynb"><img src="https://studiolab.sagemaker.aws/studiolab.svg" alt="Open In Studio Lab"></a><br> |


The Oracle DBA Console serves as the Control Center for the Oracle 23ai Hybrid Vector Database of the entire GitHub repository.
<p align="center">
<img src="https://github.com/Denis2054/RAG-Driven-Generative-AI-2nd-Edition/raw/main/commons/architecture_dba.png" width="600">
</p>
</details>


<details open>
<summary><h2>Requirements for this book</h2></summary>

Before running the code, ensure your development environment is properly configured.

- **Python:** Version 3.10+  
- **Environment Options:** Google Colab, Kaggle, or Local

</details>

<details open>
   <summary><h2>Knowledge Requirements</h2></summary>
    
- Proficiency in **Python**
- Working knowledge of **SQL** and **REST APIs**
- Foundational understanding of **LLM orchestration**
- Ability to navigate **cloud consoles**
- Comfort with **notebook-based workflows** for implementing multi-agent systems
</details>

<details open>
<summary><strong>Software & Platform Requirements</strong></summary>

- Access to a **Google Colab** environment  
- An **Oracle Cloud Free Tier** account to provision an **Autonomous Database 23ai** instance  
- An **OpenAI API key** for powering reasoning engines and fine‑tuning pipelines  

</details>


<details open>
<summary><h2>Hardware Requirements</h2></summary>
- A system capable of running a modern web browser smoothly
- Stable internet connection for cloud-based development and API usage
  </details>



<details open>
<summary><h2>Get to know the Author</h2></summary>

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
with and build upon


</details>

<details open>
  <summary><h2>Other Related Books</h2></summary>
<ul>

<li><a href="https://www.amazon.com/dp/1806690055">Context Engineering for Multi-Agent Systems, First Edition</a></li>
<li><a href="https://www.amazon.com/dp/B0FDQJRB7Q">Building Business‑Ready Generative AI Systems</a></li>

</ul>
</details>



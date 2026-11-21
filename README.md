# RAG-Vocabulary-Learning-System
RAG based vocabulary learning system for CET4/CET6, generates exam-style example sentences and word roots analysis.
## ✨ Features
Generate CET-style example sentences and root & affix parsing for English words.
Adopt RAG to retrieve real exam corpus, reduce LLM hallucination, improve the accuracy of generated content.
## 🛠 Tech Stack
- Python
- LangChain
- Chroma vector store
- text-embedding embedding model
- MySQL
- Streamlit
## 📌 Core Logic
1. Corpus preprocessing: split CET4/CET6 exam text into chunks, chunk size=15 token, overlap=3 token
2. Embedding and store chunks into Chroma
3. Retrieve top-3 relevant corpus by similarity when receiving a word query
4. Structured prompt + regex format check to constrain LLM output
5. API wrapper with retry, timeout and rate-limit handling
6. Store query history in MySQL
7. Streamlit web UI for interactive access, support multi-user access

## 📊 Evaluation
Tested on 100 high-frequency CET words. Compare raw LLM output and RAG-enhanced output.
Evaluation metrics: context fitness, factual accuracy (1-5 score).
Average score rises from 3.1 to 4.2 after introducing RAG.
Content generation time reduced from 12 min to 4.8 min per word.

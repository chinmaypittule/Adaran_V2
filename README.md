# Adaran_V2

**Adaran_V2** is an intelligent, local-first chatbot designed to answer questions about the Jindal School of Management (JSOM) at UT Dallas. It is built using state-of-the-art NLP tools and a Retrieval-Augmented Generation (RAG) pipeline for accurate, contextual, and source-linked answers.

> “We didn’t just build Adaran. We built ourselves.” — Team Reflection

---

## 📍 Overview

Adaran is your intelligent JSOM guide, developed to assist students, faculty, and prospective applicants in navigating 1,500+ pages of official JSOM content. 

- Answers are grounded in real UTD sources, with clickable reference links
- Built with complete transparency and open-source tools
- No OpenAI costs — runs fully locally using Ollama and Mistral
- Designed to answer real student queries about academics, admissions, scholarships, and more

---

## 🧱 Architecture Highlights

- **Web Scraping**: Playwright + BeautifulSoup
- **Preprocessing**: Cleaning, chunking (~800 char with 2-sentence overlap), metadata tagging
- **Embedding**: `all-mpnet-base-v2` (HuggingFace)
- **Vector Store**: ChromaDB with persistent storage
- **LLM**: Mistral-Instruct via Ollama (no external API calls)
- **Frontend**: Streamlit app for local, user-friendly interaction
- **Pipeline**: RAG + custom reranker chain

---

## 📁 Project Structure

```
Adaran_V2/
├── scraping/               # UTD site scraping scripts
├── data_cleaned/           # Preprocessed and cleaned content
├── chunking/               # Text splitting logic
├── embedding/              # Embedding and ChromaDB creation
├── chroma_db/              # Local vector store
├── app.py                  # Streamlit UI app
├── qa_chain_mistral.py     # Custom QA chain with reranker
├── load_retriever.py       # Retriever loading logic
├── sitemap_excels/         # URLs from JSOM site
├── scraped_pages.json      # Combined scrape dump
```

---

## 🧠 LLM & Vector Search

### 🔹 Local Language Model: Mistral via Ollama

We use the `Mistral-Instruct` model locally with [Ollama](https://ollama.com):

```bash
ollama run mistral
```

- Instruction-tuned and optimized for short-form QA
- Zero API cost and no internet requirement
- Supports secure and reproducible local deployment

### 🔹 Vector Search with ChromaDB

Semantic search is powered by:

```python
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    model_kwargs={"device": device}
)
```

Chunks are stored using:

```python
from langchain_community.vectorstores import Chroma

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
```

---

## ⚙️ Evaluation Metrics

| Parameter         | Metric           | Status         |
|------------------|------------------|----------------|
| LLM Model        | Accuracy, Latency| ✅ 20–60s avg  |
| Prompt Template  | Answer Quality   | 🟡 Manual tuning ongoing |
| Embedding Model  | Precision        | ✅ mpnet performs well |
| Chunk Size       | Completeness     | ✅ ~800 chars + overlap |
| Retriever `k`    | Relevance Noise  | ✅ Tuned (k=10 retrieve, 5 rerank) |
| Chain Type       | QA Clarity       | ✅ Reranked QA chain |
| Robustness       | Fault Tolerance  | 🟡 Future test pending |

---

## 💬 Use Cases

Students can ask:

- 🧾 **Academics**: “What are core courses in MS Business Analytics?”
- 🎓 **Admissions**: “What are the Spring 2025 deadlines?”
- 💰 **Scholarships**: “Am I eligible for merit-based scholarships?”

---

## 🔮 Future Roadmap

- 💻 Web UI enhancements
- 🔍 Intent classification
- 📊 Analytics dashboard for user interactions
- 🧪 Testing robustness with noisy queries

---

## 📬 Contact

**Chinmay Pittule**  
📧 chinmaypittule@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/chinmaypittule)

---

> Built as part of BUAN 6390 Analytics Practicum @ UT Dallas  
> Presented by: **Group 3 — Adaran**

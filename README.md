# 🧠 Rag-App

This is a minimal yet extensible implementation of a **Retrieval-Augmented Generation (RAG)** system for Question Answering using FastAPI, Dockerized vector databases (MongoDB with Quadrant, PostgreSQL with PGVector), and HNSW indexing for efficient similarity search.

---

## 📋 Features

- ✅ FastAPI backend for modular query processing
- ✅ Integration with MongoDB + [Quadrant](https://quadrantdb.com/)
- ✅ Integration with PostgreSQL + [PGVector](https://github.com/pgvector/pgvector)
- ✅ HNSW indexing on both vector stores
- ✅ Dockerized architecture for local and cloud deployment
- ✅ Runs in WSL with a `miniconda` environment
- 🔄 Streamlit GUI under development

---

## ⚙️ Requirements

- Python 3.10 or later
- Docker + Docker Compose
- Conda / Miniconda
- WSL (Windows Subsystem for Linux) – Recommended for Windows

---

## 🐍 Environment Setup with Miniconda

1. Download [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)
2. Create and activate a new environment:

```bash
conda create -n rag_app python=3.10
conda activate rag_app
```

3. (Optional) Customize your CLI prompt:

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

---

## 📦 Installation

### Install Python Requirements

```bash
pip install -r requirements.txt
```

### Set Environment Variables

```bash
cp .env.example .env
```

Edit the `.env` file to include credentials like `OPENAI_API_KEY`, vector DB URLs, etc.

---

## 🐳 Dockerized Services

From the `/docker` directory:

```bash
cd docker
cp .env.example .env
```

Update the `.env` file for service-level credentials, then run:

```bash
docker-compose up --build
```

---

## 🚀 Run FastAPI Server

From the root of the project:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:  
📍 `http://localhost:8000`

Interactive docs:  
📖 Swagger: `http://localhost:8000/docs`  

---

## 🧪 Postman Collection

You can test the API using Postman. Import the collection from:

📂 [`/assets/rag_app.postman_collection.json`](/assets/rag_app.postman_collection.json)

> A sample Postman response will be added below once testing is finalized.

---

## 📊 Example API Response (WIP)

```json
POST /query

Request:

```

---

## 📺 Streamlit GUI [🚧 In Progress]

We're working on a visual GUI interface using Streamlit for:

- Query testing and visualization
- Document ingestion/upload
- Source-specific evaluation

Stay tuned for updates and containerized deployment via Docker!

---

## 🧱 Project Structure

```
.
├── app/                 # FastAPI app
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── vector_clients/
│   └── config/
├── docker/              # Docker Compose files
│   ├── postgres/
│   └── mongo/
├── ui/                  # Streamlit GUI (WIP)
├── assets/              # Postman files and shared assets
│   └── rag_app.postman_collection.json
├── .env.example
├── requirements.txt
└── README.md
```

---

## 📜 License

MIT License

---


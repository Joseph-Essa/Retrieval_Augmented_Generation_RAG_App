# 🚀 Retrieval Augmented Generation (RAG) App: Your Documents, Your Answers! 🧠

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- Add other cool badges: e.g., build status, stars -->
<!-- [![GitHub stars](https://img.shields.io/github/stars/Joseph-Essa/Retrieval_Augmented_Generation_RAG_App.svg?style=social&label=Star)](https://github.com/Joseph-Essa/Retrieval_Augmented_Generation_RAG_App) -->

Unlock the knowledge hidden within your documents! This RAG app intelligently combines your data with the power of cutting-edge Large Language Models (LLMs) to provide insightful, context-aware answers. Say goodbye to sifting through files and hello to instant, AI-powered wisdom.

## ✨ What Makes It Shine?

*   **Your Data, Your AI:** Upload documents, and let the app learn from them.
*   **LLM Powerhouse:** Seamlessly switch between **OpenAI, Cohere, and Google Gemini** for both understanding your documents and generating answers.
*   **Smart Retrieval:** Powered by **Qdrant** vector database for lightning-fast, relevant information lookup.
*   **Multilingual Magic:** Includes prompt templates for different languages (e.g., English, Arabic).
*   **Built for Scale:** Robust **FastAPI** backend, all neatly packaged with **Docker** for easy deployment.
*   **Developer-Friendly:** Clean architecture, configurable, and ready for your custom touches.

## 🛠️ The Tech Alchemy

*   **Backend:** Python, FastAPI
*   **LLM Integration:** Custom interfaces for OpenAI, Cohere, Gemini
*   **Vector Brain:** Qdrant
*   **Memory Vault:** MongoDB
*   **Deployment:** Docker, Docker Compose
*   **Language:** Python (>=3.9 - *confirm this!*)

## 🚀 Quick Launch Sequence

1.  **Clone the Mothership:**
    ```bash
    git clone https://github.com/Joseph-Essa/Retrieval_Augmented_Generation_RAG_App.git
    cd Retrieval_Augmented_Generation_RAG_App
    ```

2.  **Configure Your Keys to the Kingdom:**
    Copy `.env.example` to `.env` and fill in your API keys (OpenAI, Cohere, Gemini) and other settings.
    ```bash
    cp .env.example .env
    # Now, edit .env with your secrets!
    ```

3.  **Ignite with Docker Compose:**
    This command summons the entire application stack (App, MongoDB, Qdrant).
    ```bash
    docker-compose up --build -d
    ```
    *Need to shut down? `docker-compose down`*

## 📖 Explore the API Universe

Once running, your API is alive! FastAPI provides interactive documentation:

*   **Swagger UI (Playground):** `http://localhost:8000/docs`
*   **ReDoc (Reference):** `http://localhost:8000/redoc`

Test drive the endpoints using the **Postman collection** in `assets/RAG App.postman_collection.json`.

### Key Portals (Example Endpoints):

*   `POST /api/v1/files/upload`: Feed your documents to the AI.
*   `POST /api/v1/nlp/answer-question`: Ask and receive wisdom!
*   `POST /api/v1/nlp/search-chunks`: See what parts of your docs are most relevant.

## 🧠 The RAG Ritual (How It Works)

1.  **Ingest & Learn:** Documents are uploaded, broken into understandable pieces (chunks), and their essence (embeddings) is stored in Qdrant.
2.  **Question Time:** You ask a question. It's also transformed into an embedding.
3.  **Find the Clues:** Qdrant quickly finds the most relevant document chunks based on your question.
4.  **Summon the Oracle (LLM):** The question and the relevant chunks are given to your chosen LLM.
5.  **Enlightenment:** The LLM crafts an answer based on the provided information. Voilà!

## 🤝 Join the Quest (Contributing)

Got ideas? Found a bug? Want to add more magic? Contributions are highly encouraged!

1.  Fork it!
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request!

## 📜 The Sacred Scrolls (License)

Licensed under the MIT License. See the `LICENSE` file for the ancient legal runes.


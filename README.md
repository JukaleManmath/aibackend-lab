# 🧠 AIBackend-Lab — AI-Augmented Backend Playground

AIBackend-Lab is a modular backend system built to explore the integration of modern LLMs into real-world backend architectures using FastAPI, PostgreSQL, Redis, Ollama, and ChromaDB.  
Developed as part of a 30-day roadmap to become an AI-integrated backend engineer in 2025.

---

## 🚀 Features Implemented 

### ✅ Core Backend
- 🔧 **FastAPI + PostgreSQL**: Async backend with a modular structure
- 🔐 **JWT Auth + Role-Based Access Control (RBAC)**: Secure user access system

### 🤖 LLM-Driven Tools
- 🧠 **Password Strength Advisor**: Uses local Mistral model via Ollama to provide password feedback
- ⚙️ **Function Calling**: LLM decides which registered backend function to invoke using JSON schema
- 🧾 **Log Summarization**: Converts raw log data into human-readable summaries using local LLM

### 🔍 RAG + Semantic Search
- 🧠 **ChromaDB Integration**: Stores log embeddings using `sentence-transformers`
- 💬 **RAG-Based Chat with Logs**: Conversational API over logs with retrieval-augmented generation

### 🌐 Real-Time LLM Streaming
- 🌊 **WebSocket API**: Streams live LLM-generated responses using Ollama (Mistral model)

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.10+
- **Auth**: JWT, OAuth2, Pydantic
- **LLMs**: Mistral via Ollama (local), Sentence-Transformers
- **Vector Store**: ChromaDB
- **Database**: PostgreSQL
- **Realtime**: FastAPI WebSockets
- **DevOps**: (Planned) Docker, Redis

---

## 📁 Project Structure

```

aibackend-lab/
├── app/
│   ├── routes/                # Route handlers
│   ├── auth/                   # auth setup
│   ├── database/             # database Configs 
│   ├── services/         # Business logic & AI tools
│   ├── schemas/            # Pydantic models
│   │── models/            # database models
│   └── vectorestore/            # Embedding, streaming, helpers
├── requirements.txt         # requirements.txt + env files              
├── .env.example
└── README.md

````

---

## 🧪 Running Locally (Without Docker)

### ⚙️ Prerequisites

- Python 3.10+
- PostgreSQL installed and running locally
- [Ollama](https://ollama.com/) installed with a model like `mistral`
- `virtualenv` or `venv` recommended

### 🚀 Steps

```bash
# 1. Clone the repository
git clone https://github.com/JukaleManmath/aibackend-lab.git
cd aibackend-lab

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Then edit `.env` with your local DB credentials and configs

# 5. Start PostgreSQL manually (if not already running)

# 6. Run Ollama in another terminal
ollama run mistral

# 7. Start the FastAPI server
uvicorn app.main:app --reload
````

### 🔗 API Docs

Once running, visit:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📸 Key Endpoints

| Endpoint                  | Description                               |
| ------------------------- | ----------------------------------------- |
| `POST /auth/login`        | JWT login                                 |
| `POST /password-feedback` | Get feedback from LLM for a password      |
| `POST /summarize-logs`    | Send logs and receive summarized insights |
| `POST /chat/logs`         | Chat with logs via RAG                    |
| `GET /ws/chat`            | WebSocket stream for real-time LLM chat   |

---

## 🔄 In Progress (Upcoming Days)

* Resume Ranker using Embeddings (Day 9)
* Whisper-powered Voice Transcription (Day 11)
* Multi-Agent Task Planner (Day 16)
* PDF Upload + Q\&A via LLM (Day 19)

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Manmath Jukale**
[Portfolio](https://manmath-jukale-portfolio.vercel.app) | [GitHub](https://github.com/JukaleManmath) | [LinkedIn](https://linkedin.com/in/jukalemanmath)



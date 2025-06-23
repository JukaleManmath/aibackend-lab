
# 🧠 AIBackend-Lab — AI-Augmented Backend Playground

AIBackend-Lab is a modular backend system built to explore the integration of modern LLMs into real-world backend architectures using FastAPI, PostgreSQL, Redis, Ollama, and ChromaDB.  
Developed as part of a 30-day roadmap to become an AI-integrated backend engineer in 2025.

---

## 🚀 Features Implemented (Days 1–8)

### ✅ Core Backend
- 🔧 **FastAPI + PostgreSQL + Docker**: Production-ready async backend setup
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
- **Cache/Broker**: Redis (future integration)
- **DevOps**: Docker, Docker Compose

---

## 📁 Project Structure

```

aibackend-lab/
├── app/
│   ├── api/              # Route handlers
│   ├── core/             # Configs, auth setup
│   ├── services/         # Business logic & AI tools
│   ├── schemas/          # Pydantic models
│   └── utils/            # Embedding, streaming, helpers
├── scripts/              # Data setup & helper scripts
├── requirements/         # requirements.txt + env files
├── docker/               # Docker configurations
├── .env.example
└── README.md

````

---

## 🧪 Running Locally

### ⚙️ Prerequisites
- Python 3.10+
- Docker + Docker Compose
- [Ollama installed](https://ollama.com/) locally with a model like `mistral`

### 🚀 Start the App

```bash
# 1. Clone the repository
git clone https://github.com/JukaleManmath/aibackend-lab.git
cd aibackend-lab

# 2. Start Docker services
docker-compose up --build

# 3. Run Ollama in another terminal
ollama run mistral

# 4. Access the app
http://localhost:8000/docs
````

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





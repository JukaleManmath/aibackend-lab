# GitHub_Issues.md – Day 3 to Day 14 (AI + Backend Roadmap)


## 🔄 Day 3 – Password Feedback Using Mistral LLM

**Description**  
Use Mistral via Ollama to suggest stronger passwords.  
Create `/password-feedback` endpoint.  
Send weak password to LLM and return an improved version.

**Checklist**
- [ ] Setup Ollama + Mistral locally  
- [ ] Connect route to LLM  
- [ ] Prompt template for better passwords  
- [ ] Return improvement suggestion  

---

## ⏳ Day 4 – Function Calling with LLM

**Description**  
Build an LLM route that selects and executes predefined functions.  
Use JSON schema or tool list for registration.  
Parse response and call correct function.

**Checklist**
- [ ] Create `/function-call` route  
- [ ] Register functions with arguments  
- [ ] Parse `tool_use` JSON from LLM  
- [ ] Match and execute function  

---

## ⏳ Day 5 – Log Summarization with Mistral

**Description**  
Send logs to LLM for summarization.  
Store summaries in DB for later viewing.

**Checklist**
- [ ] Accept logs via `/summarize-logs`  
- [ ] Prompt Mistral for summary  
- [ ] Save summaries in database  
- [ ] Return response to user  

---

## ⏳ Day 6 – Setup Vector DB + RAG with Chroma

**Description**  
Embed and store text chunks in ChromaDB.  
Retrieve context for new queries.

**Checklist**
- [ ] Install & configure ChromaDB  
- [ ] Use sentence-transformers to embed  
- [ ] Create `/embed`, `/retrieve` endpoints  
- [ ] Return similar chunks  

---

## ⏳ Day 7 – RAG Chat with Logs

**Description**  
Query logs using LLM + Chroma vector search.

**Checklist**
- [ ] `/chat-logs` route  
- [ ] Use context from embeddings  
- [ ] Handle chat history  
- [ ] Return coherent LLM response  

---

## ⏳ Day 8 – WebSocket-Based LLM Chat

**Description**  
Enable real-time responses from LLM via WebSocket.

**Checklist**
- [ ] Create `/ws/chat` WebSocket route  
- [ ] Stream LLM response chunk by chunk  
- [ ] Handle disconnects and reconnects  
- [ ] Basic frontend or curl test  

---

## ⏳ Day 9 – Resume Scorer with Local Embeddings

**Description**  
Compare resumes to job descriptions using similarity scores.

**Checklist**
- [ ] Accept resume and JD text  
- [ ] Embed with sentence-transformers  
- [ ] Cosine similarity + ranking  
- [ ] Return score + LLM feedback  

---

## ⏳ Day 10 – Deploy to Render

**Description**  
Deploy API with PostgreSQL to Render.com.

**Checklist**
- [ ] Gunicorn setup  
- [ ] Environment variables (.env.prod)  
- [ ] Docker + docker-compose.prod.yml  
- [ ] Connect hosted PostgreSQL  
- [ ] Verify live endpoints  

---

## ⏳ Day 11 – Voice-to-Text with Whisper

**Description**  
Convert uploaded audio files to text.

**Checklist**
- [ ] `/transcribe-audio` route  
- [ ] Accept .mp3/.wav uploads  
- [ ] Run Whisper locally or via HF  
- [ ] Return JSON transcript  

---

## ⏳ Day 12 – Task Scheduler with LLM Planning

**Description**  
Accept user intent → generate cron-style task schedules.

**Checklist**
- [ ] `/schedule-task` endpoint  
- [ ] Prompt to convert to schedule  
- [ ] Validate cron expression  
- [ ] Store task config in DB  

---

## ⏳ Day 13 – Image Captioning with LLaVA

**Description**  
Describe screenshots with a visual model.

**Checklist**
- [ ] `/caption-image` endpoint  
- [ ] Upload image  
- [ ] Run through LLaVA  
- [ ] Return summary/caption  

---

## ⏳ Day 14 – Visual Classifier with LLaVA

**Description**  
Use vision model to tag UI components from screenshots.

**Checklist**
- [ ] `/classify-screenshot` endpoint  
- [ ] Feed image to LLaVA  
- [ ] Return list of UI components  

---

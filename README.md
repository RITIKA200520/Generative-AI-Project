<div align="center">

# 🤖 Generative AI Project

### An interactive AI Mood Chatbot powered by Google Gemini & LangChain

[![Streamlit App](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://generative-ai-project-jixrdy5pjbph3snjepa47l.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.4-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-2.0-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)

</div>

---

## 🌐 Live Demo

> **Try it now →** [https://generative-ai-project-jixrdy5pjbph3snjepa47l.streamlit.app/](https://generative-ai-project-jixrdy5pjbph3snjepa47l.streamlit.app/)

No installation needed. Just open the link, enter your Google API key, and start chatting!

---

## 📌 What This Project Does

This project explores **Generative AI** concepts hands-on — from building conversational chatbots with personality modes to working with text embeddings. The flagship feature is a fully deployed **AI Mood Chatbot** that changes its personality based on your choice.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                          │
│                   (Streamlit Web Interface)                   │
└──────────────────────────┬──────────────────────────────────┘
                           │  HTTP
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT CLOUD                            │
│                                                               │
│   ┌─────────────┐    ┌──────────────┐    ┌───────────────┐  │
│   │  Mode       │    │  Session     │    │  Sidebar      │  │
│   │  Selector   │    │  State       │    │  API Key      │  │
│   │ 😡 😂 😢 😊  │    │  (History)   │    │  Input        │  │
│   └──────┬──────┘    └──────┬───────┘    └───────┬───────┘  │
│          │                  │                    │            │
│          └──────────────────┴────────────────────┘            │
│                             │                                  │
│                    ┌────────▼────────┐                        │
│                    │   LangChain     │                        │
│                    │   Orchestrator  │                        │
│                    └────────┬────────┘                        │
└─────────────────────────────┼───────────────────────────────┘
                              │  API Call
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   GOOGLE GEMINI API                           │
│              (gemini-2.0-flash-lite model)                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Chatbot Flow Pipeline

```
User Input
    │
    ▼
┌─────────────────┐
│  Select Mode    │  ← 😡 Angry / 😂 Funny / 😢 Sad / 😊 Normal
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ System Message  │  ← Personality prompt injected
│ (Persona)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Chat History    │  ← Full conversation context kept in session
│ (Memory)        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  LangChain      │
│  ChatGoogleGen  │  ← model.invoke(messages)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Gemini 2.0     │  ← Generates response based on persona + history
│  Flash Lite     │
└────────┬────────┘
         │
         ▼
   AI Response
   displayed in
   chat bubble
```

---

## 📁 Project Structure

```
Generative-AI-Project/
│
├── app.py                          ← 🚀 Main Streamlit app (entry point)
│
├── chatmodels/
│   ├── UIchatbot.py                ← Streamlit UI chatbot (alternate entry)
│   ├── chatbot.py                  ← CLI chatbot with mood modes
│   ├── chat.py                     ← Basic CLI chatbot
│   └── localmodel.py               ← HuggingFace local model demo
│
├── embeddingmodels/
│   └── huggingface_embedding.py    ← Text embedding with sentence-transformers
│
├── .streamlit/
│   └── config.toml                 ← Dark theme configuration
│
├── requirements.txt                ← Python dependencies
└── pyproject.toml                  ← Project metadata
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎭 **4 AI Personalities** | Angry, Funny, Sad, and Normal modes |
| 🧠 **Conversation Memory** | Full chat history maintained per session |
| 🔑 **Flexible API Key** | Via Streamlit Secrets, `.env`, or sidebar input |
| 🌙 **Dark Theme** | Custom dark purple UI |
| ♻️ **Clear Chat** | Reset conversation while keeping the same mode |
| ⚡ **Gemini 2.0** | Powered by Google's latest flash model |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **AI Orchestration** | LangChain |
| **Language Model** | Google Gemini 2.0 Flash Lite |
| **Embeddings** | HuggingFace `sentence-transformers` |
| **Language** | Python 3.12 |
| **Package Manager** | UV |
| **Deployment** | Streamlit Cloud |

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/RITIKA200520/Generative-AI-Project.git
cd Generative-AI-Project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
echo 'GOOGLE_API_KEY="your-key-here"' > .env

# 4. Launch the app
streamlit run app.py
```

Get a free API key at [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

---

## 📚 Modules Overview

### 1. 🤖 AI Mood Chatbot (`app.py`)
The main Streamlit web app. Users pick a personality mode and chat with an AI that responds accordingly — aggressively when angry, with jokes when funny, emotionally when sad, or helpfully in normal mode.

### 2. 💬 CLI Chatbots (`chatmodels/`)
Terminal-based chatbot scripts for experimenting with LangChain's message types (`SystemMessage`, `HumanMessage`, `AIMessage`) and multi-turn conversation logic.

### 3. 📐 Text Embeddings (`embeddingmodels/`)
Demonstrates how sentences are converted to numerical vectors using HuggingFace's `sentence-transformers/all-MiniLM-L6-v2` — the foundation of semantic search and RAG systems.

---

<div align="center">

*Built as part of a hands-on learning journey in Generative AI and LLM application development.*

</div>

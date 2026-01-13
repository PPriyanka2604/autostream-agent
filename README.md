AutoStream – Social-to-Lead Agentic Workflow

This repository contains a conversational AI agent built as part of the Machine Learning Intern assignment for ServiceHive (Inflx).

The agent represents a fictional SaaS product called AutoStream, which provides automated video editing tools for content creators.
Its purpose is to convert conversations into qualified business leads using intent detection, retrieval-augmented generation (RAG), and controlled tool execution.

🚀 Key Features

Intent detection (greeting, product/pricing inquiry, high-intent lead)

RAG-powered responses using a local knowledge base

Multi-turn, stateful conversations using LangGraph

Safe and controlled lead-capture tool execution

FastAPI backend with a professional web-based chat UI

🧠 Knowledge Base

The agent retrieves information from a local knowledge base containing:

Pricing & Features

Basic Plan – $29/month

10 videos per month

720p resolution

Pro Plan – $79/month

Unlimited videos

4K resolution

AI-generated captions

Company Policies

No refunds after 7 days

24/7 support available only on the Pro plan

The knowledge base is stored locally and accessed through a FAISS vector store.

🛠 Tech Stack

Language: Python 3.9+

Framework: LangChain + LangGraph

LLM: Groq-compatible LLM (via LangChain)

Backend: FastAPI

Frontend: HTML, CSS, JavaScript

Vector Store: FAISS

State Management: LangGraph state

📁 Project Structure
```
autostream-agent/
├── backend/
│   ├── agent/
│   │   ├── graph.py        # LangGraph workflow definition
│   │   ├── intent.py       # Intent detection logic
│   │   ├── rag.py          # RAG pipeline (FAISS + embeddings)
│   │   ├── llm.py          # LLM integration
│   │   ├── state.py        # Conversation state schema
│   │   └── tools.py        # Mock lead capture tool
│   ├── data/
│   │   └── knowledge_base.md
│   ├── app.py              # FastAPI application
│   └── main.py             # Local testing entry point
│
├── frontend/
│   ├── index.html          # Chat UI
│   ├── style.css           # UI styling
│   └── script.js           # Frontend logic
│
├── requirements.txt
├── README.md
└── demo.mp4 (or demo video link)
```

▶️ How to Run the Project Locally
1️⃣ Clone the repository
```
git clone <your-github-repo-url>
cd autostream-agent
```
2️⃣ Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate    # Windows
```
3️⃣ Install dependencies
```
pip install -r requirements.txt

```
4️⃣ Set environment variables

Create a .env file in the project root:
```
GROQ_API_KEY=your_api_key_here
```
5️⃣ Start the backend server
```
uvicorn backend.app:app
```
6️⃣ Open the frontend

Open frontend/index.html in your browser.

🧩 Architecture Explanation

This project uses LangGraph to implement a structured, agentic conversational workflow rather than a simple chatbot. LangGraph was chosen because it enables explicit control over conversation flow, state transitions, and tool execution — all of which are essential for real-world lead-generation systems.

The agent begins by performing intent detection, classifying each user message as a greeting, product inquiry, or high-intent lead. For product-related questions, a Retrieval-Augmented Generation (RAG) pipeline retrieves relevant context from a local knowledge base stored in a FAISS vector database. This grounding step ensures accurate and non-hallucinatory responses.

When high intent is detected, the agent transitions into a lead qualification workflow. Using LangGraph state, it collects the user’s name, email, and creator platform across multiple conversation turns while maintaining context. Only after all required fields are collected does the agent trigger a backend tool (mock_lead_capture) to simulate lead submission.

This design ensures safe tool usage, clean state management, and a scalable architecture suitable for production environments.

📲 WhatsApp Deployment 

To deploy this agent on WhatsApp, the FastAPI backend can be integrated with the WhatsApp Business API using webhooks. Incoming WhatsApp messages would be forwarded to the /chat endpoint, and the agent’s responses would be sent back via the WhatsApp API. LangGraph state can be stored per user session (using the phone number as a unique identifier) to preserve conversation continuity across messages.
```
🎥 Demo Video

The demo video showcases:

RAG-based pricing responses

High-intent detection

Lead qualification (name, email, platform)

Successful mock lead capture tool execution

🔗 Demo Video:
https://drive.google.com/file/d/19uBrul0jP-UzxxBkQJ4eC2aVMCBJXx_Z/view?usp=sharing
```
✅ Summary

This project demonstrates a real-world Social-to-Lead AI agent with:

Reliable intent detection

Knowledge-grounded responses

Multi-turn stateful workflows

Controlled backend tool execution

It is designed to be easily extensible for production use cases such as website chat assistants or WhatsApp-based lead generation systems.

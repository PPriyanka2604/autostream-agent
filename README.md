# AutoStream – Social-to-Lead Agentic Workflow

This project is a conversational AI agent built as part of the **Machine Learning Intern assignment** for **ServiceHive (Inflx)**.

The agent represents a fictional SaaS product called **AutoStream**, which provides automated video editing tools for content creators.  
Its goal is to convert user conversations into **qualified business leads** using intent detection, retrieval-augmented generation (RAG), and controlled tool execution.

---

## 🚀 Features

- Intent detection (greeting, product inquiry, high-intent lead)
- RAG-powered answers using a local knowledge base
- Multi-turn stateful conversation handling
- Safe lead capture tool execution
- FastAPI backend with a web-based chat UI

---

## 🧠 Knowledge Base

The agent retrieves information from a local knowledge base containing:

### Pricing & Features
- **Basic Plan** – $29/month  
  - 10 videos/month  
  - 720p resolution  

- **Pro Plan** – $79/month  
  - Unlimited videos  
  - 4K resolution  
  - AI captions  

### Policies
- No refunds after 7 days  
- 24/7 support available only on the Pro plan  

---

## 🛠 Tech Stack

- **Language:** Python 3.9+
- **Framework:** LangChain + LangGraph
- **LLM:** Groq-compatible LLM (via LangChain)
- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Vector Store:** FAISS
- **State Management:** LangGraph state

---

## ▶️ How to Run the Project Locally

### 1. Clone the repository
```bash
git clone <your-github-repo-url>
cd autostream-agent
2. Create and activate a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Start the backend server
bash
Copy code
uvicorn backend.app:app
5. Open the frontend
Open frontend/index.html in your browser.

🧩 Architecture Explanation 
This project uses LangGraph to implement a structured, agentic conversational workflow instead of a simple chatbot. LangGraph was chosen because it allows explicit control over conversation flow, state transitions, and tool execution, which is critical for real-world lead generation systems.

The agent first performs intent detection to classify the user’s message into one of three categories: greeting, product inquiry, or high-intent lead. For product-related queries, the agent uses a Retrieval-Augmented Generation (RAG) pipeline that retrieves relevant information from a local knowledge base stored in a vector database (FAISS). This prevents hallucinations and ensures accurate, grounded responses.

When high intent is detected, the agent transitions into a lead qualification flow. Using LangGraph state, it collects the user’s name, email, and creator platform across multiple turns while retaining conversation context. Only after all required fields are collected does the agent trigger a backend tool (mock_lead_capture) to simulate lead submission.

This design ensures safe tool usage, clean state management, and a scalable architecture suitable for production environments.

📲 WhatsApp Deployment (Conceptual)
To deploy this agent on WhatsApp, the FastAPI backend can be integrated using WhatsApp Business API webhooks. Incoming WhatsApp messages would be forwarded to the /chat endpoint, and the agent’s response would be sent back to the user via the WhatsApp API. The LangGraph state can be stored per user (using phone number as session ID) to maintain conversation continuity across messages.

## 🎥 Demo Video

A short demo showcasing:
- RAG-based pricing responses
- High-intent detection
- Lead qualification (name, email, platform)
- Mock lead capture tool execution

🔗 Demo Video:  
https://drive.google.com/file/d/19uBrul0jP-UzxxBkQJ4eC2aVMCBJXx_Z/view?usp=sharing

✅ Summary
This project demonstrates a real-world Social-to-Lead AI agent with:

Reliable intent detection

Knowledge-grounded responses

Multi-turn stateful workflows

Controlled backend tool execution

It is designed to be extensible for real production use cases such as WhatsApp or website chat assistants.
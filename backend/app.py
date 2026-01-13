from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.agent.graph import build_graph


# Initialize FastAPI
app = FastAPI(
    title="AutoStream Agent API",
    description="Social-to-Lead Conversational AI for AutoStream",
    version="1.0.0"
)

# Enable CORS (for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for local/demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Build LangGraph agent once at startup
graph = build_graph()


# Request schema
class ChatRequest(BaseModel):
    message: str


# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    """
    Accepts a user message and returns agent response.
    """
    result = graph.invoke({"user_input": req.message})
    return {"response": result["response"]}


# Health check (optional but professional)
@app.get("/")
def health():
    return {"status": "AutoStream Agent running"}

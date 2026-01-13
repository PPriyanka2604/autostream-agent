import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

def generate_response(context: str, user_query: str) -> str:
    prompt = f"""
You are AutoStream's AI assistant.
Answer ONLY using the context below.

Context:
{context}

User question:
{user_query}
"""
    response = llm.invoke(prompt)
    return response.content

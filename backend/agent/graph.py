from langgraph.graph import StateGraph, END

from backend.agent.state import AgentState
from backend.agent.intent import detect_intent
from backend.agent.rag import get_retriever
from backend.agent.llm import generate_response
from backend.agent.tools import mock_lead_capture


# -------------------------
# Node functions
# -------------------------

def router(state: AgentState):
    # Detect intent only if it is not already set
    if not state.get("intent"):
        state["intent"] = detect_intent(state["user_input"])
    return state



def greet(state: AgentState):
    state["response"] = (
        "Hi! 👋 I can help you with AutoStream pricing, features, "
        "or getting you started."
    )
    return state


def rag_answer(state: AgentState):
    retriever = get_retriever()
    docs = retriever.invoke(state["user_input"])
    context = "\n".join([d.page_content for d in docs])

    state["response"] = generate_response(context, state["user_input"])
    return state


def ask_name(state: AgentState):
    state["response"] = "Great! May I know your name?"
    return state


def ask_email(state: AgentState):
    if not state.get("name"):
        state["response"] = "May I know your name first?"
        return state

    state["response"] = f"Thanks {state['name']}! Could you share your email?"
    return state


def ask_platform(state: AgentState):
    if not state.get("email"):
        state["response"] = "Could you share your email so I can proceed?"
        return state

    state["response"] = (
        "Which platform do you create content on? "
        "(YouTube, Instagram, etc.)"
    )
    return state


def capture_lead(state: AgentState):
    if state.get("name") and state.get("email") and state.get("platform"):
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"],
        )
        state["response"] = (
            "You're all set! 🚀 Our team will reach out to you shortly."
        )
        return state

    state["response"] = "I just need a few more details to get you started."
    return state


# -------------------------
# Routing logic
# -------------------------

def route_intent(state: AgentState):
    intent = state.get("intent")

    if intent == "greeting":
        return "greet"

    if intent == "product_inquiry":
        return "rag_answer"

    if intent == "high_intent":
        if not state.get("name"):
            return "ask_name"
        if not state.get("email"):
            return "ask_email"
        if not state.get("platform"):
            return "ask_platform"
        return "capture_lead"

    return END


# -------------------------
# Build graph
# -------------------------

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("router", router)
    graph.add_node("greet", greet)
    graph.add_node("rag_answer", rag_answer)
    graph.add_node("ask_name", ask_name)
    graph.add_node("ask_email", ask_email)
    graph.add_node("ask_platform", ask_platform)
    graph.add_node("capture_lead", capture_lead)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        route_intent,
    )

    graph.add_edge("greet", END)
    graph.add_edge("rag_answer", END)
    graph.add_edge("ask_name", END)
    graph.add_edge("ask_email", END)
    graph.add_edge("ask_platform", END)
    graph.add_edge("capture_lead", END)

    return graph.compile()

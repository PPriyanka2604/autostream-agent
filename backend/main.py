from agent.rag import get_retriever
from agent.llm import generate_response

if __name__ == "__main__":
    retriever = get_retriever()

    question = "Does the Pro plan include support?"
    docs = retriever.invoke(question)

    context = "\n".join([d.page_content for d in docs])

    answer = generate_response(context, question)
    print(answer)

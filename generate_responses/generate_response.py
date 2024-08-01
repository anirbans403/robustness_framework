from llm.call_llm import get_response


def get_answer(context, question, model):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Given a context and a question, answer the question using the context.",
        },
        {
            "role": "user",
            "content": f"""Context : 
         ```
         {context}
         ```
         Question:
         ```
         {question}
         ```
         """,
        },
    ]
    return get_response(messages, model)

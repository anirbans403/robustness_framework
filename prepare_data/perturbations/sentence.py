from llm.call_llm import get_response


def perturb_s1(query):
    return query + "@sk3krb"


def perturb_s2(inputData):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Please help me to paraphase the given message. Return only paraphased message.",
        },
        {"role": "user", "content": inputData},
    ]
    return get_response(messages, "gpt4")


def perturb_s3(inputData):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Please help me to change the syntactic structure of the sentence keeping the meaning of the sentence same. Return only the converted message only.",
        },
        {"role": "user", "content": inputData},
    ]
    return get_response(messages, "gpt4")

from llm.call_llm import get_response


def perturb_s1(query):
    """
    Introduces a sentence-level perturbation by appending a randomly generated irrelevant handle 
    (e.g., "@sk3krb") to the end of the query.

    Parameters:
    query (str): The original sentence to be perturbed.

    Returns:
    str: The sentence with an irrelevant handle appended at the end.
    """
    return query + "@sk3krb"


def perturb_s2(inputData):
    """
    Introduces a sentence-level perturbation by paraphrasing the given sentence. The function sends 
    the input data to an LLM (e.g., GPT-4) to generate a paraphrased version of the sentence.

    Parameters:
    inputData (str): The original sentence to be paraphrased.

    Returns:
    str: The paraphrased sentence returned by the LLM.
    """
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Please help me to paraphrase the given message. Return only paraphrased message.",
        },
        {"role": "user", "content": inputData},
    ]
    return get_response(messages, "gpt4")


def perturb_s3(inputData):
    """
    Introduces a sentence-level perturbation by changing the syntactic structure of the given sentence 
    while keeping its meaning intact. The function sends the input data to an LLM (e.g., GPT-4) to 
    generate a syntactically altered version of the sentence.

    Parameters:
    inputData (str): The original sentence whose syntactic structure is to be altered.

    Returns:
    str: The sentence with an altered syntactic structure returned by the LLM.
    """
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Please help me to change the syntactic structure of the sentence keeping the meaning of the sentence same. Return only the converted message only.",
        },
        {"role": "user", "content": inputData},
    ]
    return get_response(messages, "gpt4")

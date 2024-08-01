import json
import requests
import warnings
import os

warnings.filterwarnings("ignore")
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("API_KEY")
url = os.getenv("OPENAI_GATEWAY_URL")
max_length = 1000
temperature = 1.2


def get_payload(messages, llm):
    if llm == "gpt4":
        openai_payload = json.dumps(
            {
                "model": "gpt-4",
                "task": "chat/completions",
                "max_length": max_length,
                "temperature": temperature,
                "model-params": {"messages": messages},
            }
        )
        return openai_payload


def parse_open_ai_response(response):
    try:
        response_payload = response.json()
        llm_response = ""
        if "choices" in response_payload:
            choices = response_payload["choices"]
            if choices and len(choices) > 0:
                if "message" in choices[0]:
                    message = choices[0]["message"]
                    if "content" in message:
                        llm_response = message["content"]

        if llm_response is not None and isinstance(llm_response, str):
            return str(llm_response)
        else:
            return ""

    except Exception as e:
        return ""


def get_response(messages, llm):
    headers = {"X-Api-Key": api_key, "Content-Type": "application/json"}
    payload = get_payload(messages, llm)
    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False
    )
    if llm == "gpt4":
        llm_response = parse_open_ai_response(response)
    return llm_response


def parse_open_ai_response(response):
    try:
        response_payload = response.json()
        llm_response = ""
        if "choices" in response_payload:
            choices = response_payload["choices"]
            if choices and len(choices) > 0:
                if "message" in choices[0]:
                    message = choices[0]["message"]
                    if "content" in message:
                        llm_response = message["content"]

        if llm_response is not None and isinstance(llm_response, str):
            return str(llm_response)
        else:
            return ""

    except Exception as e:
        return ""

import requests
from dotenv import load_dotenv
import os
import urllib3
import uuid
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()


def get_token() -> str:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload = {"scope": "GIGACHAT_API_PERS"}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": str(uuid.uuid4()),
        "Authorization": f"Basic {os.getenv("GIGACHAT_API_KEY")}",
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False
    )
    return response.json()["access_token"]


def get_models() -> dict:
    """
    Returning all available GigaChat models
    """
    url = "https://gigachat.devices.sberbank.ru/api/v1/models"

    payload = {}
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    return response.json()


def generate_text(query: str) -> str:
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps(
        {
            "model": "GigaChat",
            "messages": [{"role": "user", "content": query}],
            "stream": False,
            "repetition_penalty": 1,
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False
    )
    print(response.json()["usage"])
    return response.json()["choices"][0]["message"]["content"]

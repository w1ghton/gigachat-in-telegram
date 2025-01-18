import requests
from dotenv import load_dotenv
import os
import urllib3
import uuid

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()


def get_token():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload = "scope=GIGACHAT_API_PERS"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": str(uuid.uuid4()),
        "Authorization": f"Basic {os.getenv("AUTH_TOKEN")}",
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False
    )
    return response.json()["access_token"]


def get_models():
    url = "https://gigachat.devices.sberbank.ru/api/v1/models"

    payload = {}
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    return response.json()


print(get_models())

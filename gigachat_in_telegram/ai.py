from gigachat import GigaChat
from dotenv import load_dotenv
import os

load_dotenv()


def generate_text(query: str) -> str:
    model = GigaChat(
        credentials=os.getenv("AUTH_TOKEN"),
        model="GigaChat",
        verify_ssl_certs=False,
    )

    response = model.chat(query)
    return response.choices[0].message.content

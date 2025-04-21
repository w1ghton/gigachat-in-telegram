from env import Settings
from gigachat import GigaChat


def generate_text(query: str) -> str:
    model = GigaChat(
        credentials=Settings().gigachat_api_key,
        model="GigaChat",
        verify_ssl_certs=False,
    )

    response = model.chat(
        payload={
            "messages": [
                {"role": "system", "content": "Отвечай кратко"},
                {"role": "user", "content": query},
            ],
            "max_tokens": 512,
        }
    )
    return response.choices[0].message.content

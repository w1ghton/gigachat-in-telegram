import re
from env import Settings
from gigachat import GigaChat


def escape_markdown_v2(text: str) -> str:
    return re.sub(r"([\[\]()>#+\-=|{}.!])", r"\\\1", text)


def generate_text(query: str) -> str:
    FORMAT_TEXT = """При необходимости форматирования используй это:
                    **Жирный текст**
                    __Текст курсивом__
                    ~~Зачеркнутый текст~~
                    `Моноширинный текст`
                    ```Несколько строк кода```"""

    model = GigaChat(
        credentials=Settings().gigachat_api_key,
        model="GigaChat",
        verify_ssl_certs=False,
    )

    response = model.chat(
        payload={
            "messages": [
                {"role": "system", "content": FORMAT_TEXT},
                {"role": "user", "content": query},
            ],
            "max_tokens": 512,
        }
    )
    return escape_markdown_v2(response.choices[0].message.content)

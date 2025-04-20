from env import Settings
from gigachat import GigaChat


def generate_text(query: str) -> str:
    FORMAT_TEXT = """При использовании форматирования используй это:
                    **Жирный текст** – две звездочки с обеих сторон текста.
                    __Текст курсивом__ – два нижних подчеркивания.
                    ~~Зачеркнутый текст~~ – две тильды.
                    `Моноширинный текст` – один знак апострофа.
                    ```Моноширинный текст 2``` – три знака апострофа, можно выделить несколько строк. Отличается от моно через контекстное меню (на маке без цвета и не копируется на Windows и MacOS при нажатии, поэтому для выделения нескольких строк лучше используйте контекстное меню)"""

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
    return response.choices[0].message.content

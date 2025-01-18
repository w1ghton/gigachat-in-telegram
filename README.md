# GigaChat в Telegram

## Требования
- Python версии 3.12 или выше.
- Установленный [Poetry](https://python-poetry.org/).

## Установка

1. **Клонирование репозитория:**

   ```bash
   git clone https://github.com/w1ghton/gigachat-in-telegram.git
   ```

2. **Переход в директорию проекта:**

   ```bash
   cd gigachat-in-telegram
   ```

3. **Установка зависимостей:**

   Убедитесь, что у вас установлена поддерживаемая версия Python. Настройте виртуальное окружение с помощью Poetry:

   ```bash
   poetry env use python3.xx  # xx - версия Python >= 3.12
   poetry install
   ```

4. **Создание файла конфигурации `.env`:**

   В корневой директории проекта создайте файл `.env` со следующим содержимым:

   ```env
   TELEGRAM_BOT_TOKEN=токен_бота
   GIGACHAT_API_KEY=ключ_авторизации_к_GigaChat
   ```

   - `TELEGRAM_BOT_TOKEN`: Токен Telegram-бота, который можно получить через [BotFather](https://t.me/botfather).
   - `GIGACHAT_API_KEY`: Ключ доступа к GigaChat, доступный в [документации GigaChat](https://developers.sber.ru/docs/ru/gigachat/api/authorization).

## Запуск

1. **Активация виртуального окружения:**

   ```bash
   eval $(poetry env activate)
   ```

2. **Запуск бота:**

   ```bash
   python -m gigachat_in_telegram
   ```

3. **Проверка работы:**

   Откройте Telegram, найдите вашего бота по имени и начните с ним диалог.

## Примечания
- Убедитесь, что вы используете российский IP-адрес, так как GigaChat недоступен из других регионов.
- При необходимости установите сертификаты для подключения к GigaChat. Подробнее читайте в [документации](https://developers.sber.ru/docs/ru/gigachat/certificates).

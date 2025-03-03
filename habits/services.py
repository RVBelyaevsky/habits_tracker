import requests
from config import settings


def send_telegram_message(chat_id, message):
    """Отправляет сообщение используя бота телеграм"""
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params
    )

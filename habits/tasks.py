from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_message_tg():
    """Напоминает пользователю у которого есть телеграмм о его привычках."""
    message = "А ты не забыл про свою полезную привычку?"
    habits = Habit.objects.filter(user__isnull=False)

    for habit in habits:
        if habit.user.tg_chat_id:
            send_telegram_message(habit.user.tg_chat_id, message)

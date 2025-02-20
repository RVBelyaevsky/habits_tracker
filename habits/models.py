from django.db import models
from config.settings import AUTH_USER_MODEL


NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    place = models.CharField(
        max_length=150,
        verbose_name="Место",
        help_text="Укажите место, в котором необходимо выполнять привычку",
    )
    time = models.DateTimeField(
        verbose_name="Время",
        help_text="Установите время, когда необходимо выполнять привычку",
    )
    action = models.CharField(
        max_length=350,
        verbose_name="Действие ",
        help_text="Укажите действие, которое представляет собой привычка",
    )
    is_enjoyable = models.BooleanField(
        verbose_name="Признак приятной привычки",
    )
    linked_habit = models.ForeignKey(
        "self", verbose_name="Связанная привычка", on_delete=models.CASCADE, **NULLABLE
    )
    periodicity = models.IntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Укажите периодичность выполнения привычки для напоминания в днях (по умолчанию ежедневная)",
    )
    reward = models.CharField(max_length=300, verbose_name="Вознаграждение", **NULLABLE)
    time_to_complete = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Время на выполнение",
        **NULLABLE
    )
    is_published = models.BooleanField(
        default=False, verbose_name="Признак публичности"
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

from datetime import timedelta, time

from rest_framework.exceptions import ValidationError


class RewardOrLinkedValidator:
    """Проверка на запрет одновременного заполнения полей reward и linked_habit."""
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if value.get('reward') and value.get('linked_habit'):
            raise ValidationError(f"reward и linked_habit одновременно заполнять нельзя")


class LimitTimeСompleteValidator:
    """Проверка времени выполнения (должно быть не больше 120 секунд)."""
    def __call__(self, value):
        time_to_complete = dict(value).get('time_to_complete')
        limit = time(hour=00, minute=2, second=00)
        if time_to_complete and time_to_complete > limit:
            raise ValidationError(f"Время выполнения должно быть не больше 120 секунд.{limit} {time_to_complete}")


class LinkedOnlyEnjoyableValidator:
    """Проверка связанной привычки на признак приятности."""
    def __call__(self, value):
        is_enjoyable = dict(value).get('is_enjoyable')
        linked_habit = dict(value).get('linked_habit')

        if not is_enjoyable and linked_habit and not linked_habit.is_enjoyable:
            raise ValidationError(f'В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class EnjoyableNotRewardNotLinked:
    """Проверка приятной привычки на вознаграждение или связанность."""

    def __call__(self, value):
        is_enjoyable = dict(value).get('is_enjoyable')
        linked_habit = dict(value).get('linked_habit')
        reward = dict(value).get('reward')

        if is_enjoyable:
            if reward or linked_habit:
                raise ValidationError(f'У приятной привычки не может быть вознаграждения или связанной привычки.')


class PeriodicityValidator:
    """Проверка на частоту выполнения привычки"""
    def __call__(self, value):
        periodicity = dict(value).get('periodicity')
        if periodicity and periodicity > 7:
            raise ValidationError(f'Неверное значение частоты выполнения привычки. Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
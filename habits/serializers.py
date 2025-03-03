from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    RewardOrLinkedValidator,
    LimitTimeСompleteValidator,
    LinkedOnlyEnjoyableValidator,
    EnjoyableNotRewardNotLinked,
    PeriodicityValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardOrLinkedValidator(field1="reward", field2="linked_habit"),
            LimitTimeСompleteValidator(),
            LinkedOnlyEnjoyableValidator(),
            EnjoyableNotRewardNotLinked(),
            PeriodicityValidator(),
        ]


class HabitPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"

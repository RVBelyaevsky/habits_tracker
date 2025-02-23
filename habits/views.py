from rest_framework import viewsets

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator

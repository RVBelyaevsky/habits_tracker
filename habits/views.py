from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer, HabitPublicSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.User = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action != 'list':
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        self.queryset = Habit.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)


class HabitPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitPublicSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator

    def get_queryset(self):
        self.queryset = Habit.objects.filter(is_published=True)
        return super().get_queryset()

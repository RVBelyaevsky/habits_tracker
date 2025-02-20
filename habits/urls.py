from rest_framework import routers

from habits.apps import HabitsConfig
from django.urls import path

from habits.views import HabitViewSet

app_name = HabitsConfig.name

router = routers.DefaultRouter()
router.register('', HabitViewSet, basename='habits')

urlpatterns = router.urls

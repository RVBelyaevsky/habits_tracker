from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'place', 'time', 'action', 'is_enjoyable', 'linked_habit', 'periodicity',
                    'reward', 'time_to_complete', 'is_published',)

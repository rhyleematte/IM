from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'date', 'time')
    list_filter = ('group', 'date')
    search_fields = ('title', 'description')

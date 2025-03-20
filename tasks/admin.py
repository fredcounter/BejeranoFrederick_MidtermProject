#FREDERICK BEJERANO
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('due_date',)

############################
# apps.py (App Configuration)
############################
from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # Default field type for primary keys
    name = 'tasks' # Name of the app


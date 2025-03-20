############################
# urls.py (Tasks App URL Configuration)
############################
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'), # Task list view
    path('create/', views.task_create, name='task_create'), # Create task view
    path('<int:id>/edit/', views.task_update, name='task_update'), # Update task view
    path('<int:id>/delete/', views.task_delete, name='task_delete'), # Delete task view
]

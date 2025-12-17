from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_task, name='add-task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete-task'),
    path('toggle/<int:task_id>/', views.toggle_status, name='toggle-status'),
    path('signup/', views.signup, name='signup'),   
]

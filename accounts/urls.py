# accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView, HomeView, RegistrationView, CalendarView, ReminderView, AddReminder, StudyGroup, Resource, AddEvent, CreateGroup,delete_task, get_reminders, add_reminder, delete_reminder,PomodoroView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('dashboard/', ReminderView.as_view(), name='dashboard'),
    path('add_reminder/', AddReminder.as_view(), name='add_reminder'),
    path('study_groups/', StudyGroup.as_view(), name='study_groups'),
    path('resource/', Resource.as_view(), name='resource'),
    path('add_event/', AddEvent.as_view(), name='add_event'),
    path('', views.index, name='index'),
    path('upload/', views.upload_resource, name='upload_resource'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_reminder/', views.add_reminder, name='add_reminder'),
    path('api/reminders/', get_reminders),
    path('api/reminders/', add_reminder),
    path('api/reminders/', delete_reminder),
    path('delete_reminder/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),
    path('meeting/',views.videocall, name='meeting'),
    path('join/',views.join_room, name='join_room'),
    path('pomodoro/', PomodoroView.as_view(), name='pomodoro'),
]



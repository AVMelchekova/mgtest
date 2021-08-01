from django.urls import path

from chemistry import views

app_name = 'chemistry'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
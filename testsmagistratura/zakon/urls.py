from django.urls import path

from zakon import views

app_name = 'zakon'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]

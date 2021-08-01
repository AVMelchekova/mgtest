from django.urls import path

from economyc import views

app_name = 'economyc'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
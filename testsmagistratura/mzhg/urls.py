from django.urls import path

from mzhg import views

app_name = 'mzhg'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
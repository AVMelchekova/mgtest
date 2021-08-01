from django.urls import path

from soilmechanics import views

app_name = 'soilmechanics'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
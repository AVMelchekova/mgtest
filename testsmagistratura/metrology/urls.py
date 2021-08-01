from django.urls import path

from metrology import views

app_name = 'metrology'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
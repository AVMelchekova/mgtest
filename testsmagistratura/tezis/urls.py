from django.urls import path

from tezis import views

app_name = 'tezis'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]

from django.urls import path

from isviv import views

app_name = 'isviv'
urlpatterns = [
    path('', views.index, name='index'),
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
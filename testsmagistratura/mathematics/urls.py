from django.urls import path

from mathematics import views

app_name = 'mathematics'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
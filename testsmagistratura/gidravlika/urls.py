from django.urls import path

from gidravlika import views

app_name = 'gidravlika'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
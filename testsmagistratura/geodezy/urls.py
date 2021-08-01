from django.urls import path

from geodezy import views

app_name = 'geodezy'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
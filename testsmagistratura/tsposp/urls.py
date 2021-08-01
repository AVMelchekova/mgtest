from django.urls import path

from tsposp import views

app_name = 'tsposp'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
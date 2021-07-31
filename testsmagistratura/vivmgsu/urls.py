from django.urls import path

from vivmgsu import views

app_name = 'vivmgsu'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]

from django.urls import path

from constructionmaterials import views

app_name = 'constructionmaterials'
urlpatterns = [
    path('quest/', views.quest, name='quest'),
    path('<int:quest_id>/verify/', views.verify, name='verify'),
]
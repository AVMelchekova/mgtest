from django.db import models


class Question(models.Model):
    question = models.TextField()


class Choice(models.Model):
    choice = models.TextField()
    correct = models.BooleanField()
    quest = models.ForeignKey(Question, on_delete=models.CASCADE)


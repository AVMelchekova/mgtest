from django.test import TestCase
from django.urls import reverse

from isviv.models import Question


def create_question(question_text, choises):
    q = Question.objects.create(question=question_text)
    for choice in choises:
        q.choice_set.create(choice=choice[0], correct=choice[1])
    return q


class QuestionVerifyViewsTests(TestCase):
    def test_empty_choice(self):
        q = create_question('Вопрос', [('ответ1', True), ('ответ2', False), ('ответ3', False)])
        response = self.client.post(reverse('verify', args=(q.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Не верно")

    def test_false_choice(self):
        q = create_question('Вопрос', [('ответ1', True), ('ответ2', False), ('ответ3', False)])
        response = self.client.post(reverse('verify', args=(q.pk,)), {'choice':2})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Не верно")

    def test_true_choice(self):
        q = create_question('Вопрос', [('ответ1', True), ('ответ2', False), ('ответ3', False)])
        response = self.client.post(reverse('verify', args=(q.pk,)), {'choice':1})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Правильно")

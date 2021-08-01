from django.shortcuts import render

from isviv.views import quest_base, verify_base
from .models import Question


def quest(request):
    q, c = quest_base(request, Question)
    context = {'quest': q,
               'choices': c,
               'title': 'Вопрос',
               'tema': 'Математика МГ',
               'action': 'mathematics:verify'}

    return render(request, 'isviv/quest.html', context)


def verify(request, quest_id):
    a, q, ch, next_q = verify_base(request, Question, quest_id)
    context = {'result': a,
               'question': q,
               'selected_choice': ch,
               'title': 'Проверка',
               'tema': 'Математика МГ',
               'next_q': next_q,
               'next_link': 'mathematics:quest'}

    return render(request, 'isviv/verify.html', context)
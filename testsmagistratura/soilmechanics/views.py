from django.shortcuts import render

from isviv.views import quest_base, verify_base
from .models import Question


def quest(request):
    q, c = quest_base(request, Question)
    context = {'quest': q,
               'choices': c,
               'title': 'Вопрос',
               'tema': 'Механика грунтов МГ',
               'action': 'soilmechanics:verify'}

    return render(request, 'isviv/quest.html', context)


def verify(request, quest_id):
    a, q, ch, next_q = verify_base(request, Question, quest_id)
    context = {'result': a,
               'question': q,
               'selected_choice': ch,
               'title': 'Проверка',
               'tema': 'Механика грунтов МГ',
               'next_q': next_q,
               'next_link': 'soilmechanics:quest'}

    return render(request, 'isviv/verify.html', context)

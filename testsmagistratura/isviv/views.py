import random

from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    title = 'Начало'
    request.session['list_q'] = []
    request.session['begin_test'] = True
    return render(request, 'isviv/index.html', {'title': title})


def quest(request):
    q, c = quest_base(request, Question)
    context = {'quest': q,
               'choices': c,
               'title': 'Вопрос',
               'tema': 'Водоснабжение и водоотведение',
               'action': 'isviv:verify'}

    return render(request, 'isviv/quest.html', context)

def quest_base(request, model_tema):
    if request.session.get('begin_test', True):
        questions = model_tema.objects.all()
        list_q = []
        for question in questions:
            list_q.append(question.pk)
        random.shuffle(list_q)
        request.session['list_q'] = list_q
        request.session['begin_test'] = False

    list_q = request.session.get('list_q', [])

    q_id = list_q.pop()
    request.session['list_q'] = list_q

    # result = Question.objects.count()
    # a = random.choice(range(result))
    q = model_tema.objects.get(pk=q_id)
    c = list(q.choice_set.all())
    random.shuffle(c)
    return q, c



def verify(request, quest_id):
    a, q, ch, next_q = verify_base(request, Question, quest_id)
    context = {'result': a,
               'question': q,
               'selected_choice': ch,
               'title': 'Проверка',
               'tema': 'Водоснабжение и водоотведение',
               'next_q': next_q,
               'next_link': 'isviv:quest'}

    return render(request, 'isviv/verify.html', context)

def verify_base(request, model_tema, quest_id):
    q = get_object_or_404(model_tema, pk=quest_id)

    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError):
        # Redisplay the question voting form.
        ch = ''
        a = 'Не верно'
    else:
        ch = selected_choice.choice
        if selected_choice.correct:
            a = 'Правильно'
        else:
            a = 'Не верно'

    list_q = request.session.get('list_q', [])
    next_q = True
    if not list_q:
        next_q = False

    return a, q, ch, next_q
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from survey.models import *


@login_required(login_url="/login/")
def index(request):
    context = {}
    questions = TextQuestion.objects.all()
    context['title'] = 'surveys'
    context['questions'] = questions
    return render(request, 'survey/index.html', context)


@login_required(login_url="/login/")
def details(request, id=None):
    context = {}
    try:
        question = TextQuestion.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    return render(request, 'survey/details.html', context)


@login_required(login_url="/login/")
def question_content(request, id=None):
    if request.method == "GET":
        context = {}
        try:
            question = TextQuestion.objects.get(id=id)
        except:
            raise Http404
        context['question'] = question
        return render(request, "survey/question_content.html", context)
    if request.method == "POST":
        user_id = 1
        data = request.POST
        ret = TextAnswer.objects.create(user_id=user_id, choice_id=data['choice'])
        if ret:
            return HttpResponse("Your vote is done successfully")
        else:
            return HttpResponse("Your vote is not done successfully")

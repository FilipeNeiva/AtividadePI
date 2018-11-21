from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pools.models import *


def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def exibir(request, id_question):

    question = Question.objects.get(id = id_question)
    choices = question.question_choice.all()

    return render(request, 'question.html', {'question': question}, {'choices': choices})
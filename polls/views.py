#httpとtemplateの読み込みをまとめて行ってくれる
from django.shortcuts import render
# from django.http import HttpResponse  # http通信を行う
# from django.template import loader # templateの読み込みを行う
from .models import Question # Questionモデルをインポート

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
      'latest_question_list' :latest_question_list,
    }
    return render(request,'polls/index.html', context)

def detail(request, question_id):
    details = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'details': details })

def results(request, question_id):
    response = "you're looking at the results of question %s."
    return render(response % question_id)

def vote(request, question_id):
    return render("you're voting on question %s." % question_id)
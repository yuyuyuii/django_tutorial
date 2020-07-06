#httpとtemplate, 404の処理をまとめて行ってくれるショートカット
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse  # http通信を行う
# from django.template import loader # templateの読み込みを行う
# from django.http import Http404 # 404エラー処理

from .models import Question  # Questionモデルをインポート

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
      'latest_question_list' :latest_question_list,
    }
    return render(request,'polls/index.html', context)

def detail(request, question_id):
  # ショートカット前
  '''
  #リクエストしたIDが存在した時
  try:
    question = Question.objects.get(pk=question_id)
  #リクエストしたIDが存在しなかった時
  except Question.DoesNotExist:
    raise Http404('Question does not exist')
  '''
  # ショートカット後, 上の処理を簡潔に書いたやつ
  question = get_object_or_404(Question, pk=question_id) # オブジェクトがあればオブジェクト, なければ404を返す
  return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "you're looking at the results of question %s."
    return render(response % question_id)

def vote(request, question_id):
    return render("you're voting on question %s." % question_id)
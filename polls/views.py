#httpとtemplate, 404の処理をまとめて行ってくれるショートカット
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect  # http通信を行う
# from django.template import loader # templateの読み込みを行う
# from django.http import Http404 # 404エラー処理
from django.urls import reverse 
from django.views import generic

from .models import Question, Choice  # Question, Choiceモデルをインポート

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#       'latest_question_list' :latest_question_list,
#     }
#     return render(request,'polls/index.html', context)

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list' # Questionモデルのデータをlatest_question_listに入れてテンプレートへ渡す

  def get_queryset(self):
    return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id):
#   # ショートカット前
#   '''
#   #リクエストしたIDが存在した時
#   try:
#     question = Question.objects.get(pk=question_id)
#   #リクエストしたIDが存在しなかった時
#   except Question.DoesNotExist:
#     raise Http404('Question does not exist')
#   '''
#   # ショートカット後, 上の処理を簡潔に書いたやつ
#   question = get_object_or_404(Question, pk=question_id) # オブジェクトがあればオブジェクト, なければ404を返す
#   return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
  model = Question # Questionモデルのデータを渡す。ルーティングでidは渡っているのでQuestionモデルの中でIDをもとにデータを返す
  template_name = 'polls/detail.html'

# def results(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'


def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "you didn't select a choice.",
      })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
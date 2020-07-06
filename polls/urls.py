from django.urls import path
from . import views  # カレントディレクトリのviews.pyをインポート

urlpatterns = [
  # /polls/
    path('', views.index, name="index"),  # path('パス名', テンプレート, アクション名(省略可))
  # /polls/2/
    path('<int:question_id>/', views.detail, name="detail"),
  # /polls/2/results/  
    path('<int:question_id>/results', views.results, name="results"),
  # /polls/2/vote/
    path('<int:question_id>/vote', views.vote, name="vote"),

]

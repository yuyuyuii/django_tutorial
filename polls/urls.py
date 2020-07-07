from django.urls import path
from . import views  # カレントディレクトリのviews.pyをインポート

app_name = "polls"
urlpatterns = [
  # /polls/
    path('', views.IndexView.as_view(), name="index"),  # path('パス名', テンプレート, アクション名(省略可))
  # /polls/2/
    # path('<int:question_id>/', views.detail, name="detail"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
  # /polls/2/results/  
    # path('<int:question_id>/results', views.results, name="results"),
    path('<int:pk>/results', views.ResultsView.as_view(), name="results"),
  # /polls/2/vote/
    path('<int:question_id>/vote', views.vote, name="vote"),
]

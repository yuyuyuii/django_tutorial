from django.urls import path
from . import views  # カレントディレクトリのviews.pyをインポート

urlpatterns = [
    path('', views.index, name="index"), # path('パス名', テンプレート, アクション名(省略可))
]

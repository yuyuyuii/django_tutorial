import datetime
from django.utils import timezone
from django.db import models
# モデルの定義が終わったらpractice/setting.pyのINSTALLED_APPSへpollsモデルを追加する

class Question(models.Model):
  question_text = models.CharField(max_length=200) #CharFieldの引数にはmax_lengthを必ず指定する必要がある
  pub_date = models.DateTimeField('date published')
  def __str__(self):
      return self.question_text

  def was_published_recently(self):
      return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  


class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE) # リレーションの設定
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
      return self.choice_text
  

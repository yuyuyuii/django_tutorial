from django.contrib import admin

from .models import Question, Choice # djangoの管理画面でQuestionモデルを管理する為に追加

class ChoiceInline(admin.TabularInline): #Choiceを作成するときにデフォルトで３つ作成すると宣言
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin): # 管理画面のquestion修正時に日付とテキストのフィールドの順番を変更している
  # fields = ['pub_date', 'question_text']
  fieldsets = [
    (None, {'fields': ['question_text']}),# タイトルを追加することができる
    ('Date infomation', {'fields': ['pub_date']})
  ]
  inlines = [ChoiceInline] # questionを作成するときにchoiceを３つ表示させる


admin.site.register(Question, QuestionAdmin)  # 管理画面にQuestionモデルを登録
admin.site.register(Choice)
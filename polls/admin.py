from django.contrib import admin

from .models import Question # djangoの管理画面でQuestionモデルを管理する為に追加

admin.site.register(Question) # 管理画面にQuestionモデルを登録
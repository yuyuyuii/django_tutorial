from django.shortcuts import render
from django.http import HttpResponse # http通信を行う

def index(request):
  return HttpResponse('hello world')

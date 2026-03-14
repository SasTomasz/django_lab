from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return HttpResponse(articles)

class NameView(View):
    def get(self, request, *args, **kwargs):
        data = []
        for i in kwargs.items():
            data.append(i)
        return HttpResponse(data)

class NameExperimentView(View):
    def get(self, request, *args, **kwargs):
        data = []
        for i in args:
            data.append(i)
        return HttpResponse(data)
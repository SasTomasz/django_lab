from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.base import RedirectView

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


# Basic use of View class,
# see https://docs.djangoproject.com/en/6.0/topics/class-based-views/intro/#using-class-based-views
class Test01(View):
    def get(self, request):
        return HttpResponse("Test-01")


class Test02(View):
    def get(self, request):
        return HttpResponse("Test-02")


# More about how redirect works can be found on
# https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#redirectview
class ArticleCounterRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "article-detail"

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)


class ArticleDetailView(View):
    def get(self, request, **kwargs):
        return HttpResponse(f"Redirect from another page + arguments: {kwargs.items()}")

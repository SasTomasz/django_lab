from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView

from . import models


def article_list(request):
    articles = models.Article.objects.all()
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
        article = get_object_or_404(models.Article, pk=kwargs["pk"])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)


class ArticleDetailView(View):
    def get(self, request, **kwargs):
        return HttpResponse(f"Redirect from another page + arguments: {kwargs.items()}")


# The following class are example how to inherit an attribute and method from parent class and how to override them
class GreetingView(View):
    # Add a new attribute to class View
    greeting = "Hello"

    # Overriding a function get() from parent class
    def get(self, request):
        return HttpResponse(self.greeting)


class GreetingChildView(GreetingView):
    # attribute is overriding
    greeting = "Morning to ya"


class PublisherListView(ListView):
    model = models.Publisher
    template_name = 'blog/publishers.html'

# class DetailView can add more context as clas ListView so with DetailView class more the one model
# can be pass to template
class PublisherDetailView(DetailView):
    model = models.Publisher
    template_name = 'blog/publishers-detail.html'
    # This is method to get more context
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["book_list"] = models.Book.objects.all()
        print(f"DEBUG: {context["book_list"]}")
        return context

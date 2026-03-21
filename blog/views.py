import logging

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView

from . import models

logger = logging.getLogger("django")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
)


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
        logger.info(f"Context --> {context}")
        # Add in a QuerySet of all the books
        context["book_list"] = models.Book.objects.filter(publisher=kwargs["object"])

        logger.info(f"context[book_list] --> {context["book_list"]}")
        logger.info(f"kwargs --> {kwargs}")
        return context


class PublisherTwoDetailView(DetailView):
    context_object_name = "publisher"
    queryset = models.Publisher.objects.all()
    template_name = 'blog/publishers-2-detail.html'

    # DetailView class is design in way that return particular object (with particular pk passed within kwargs)
    # To change behavior or add more data to that generic view we can use get_context_data func. where is the
    # possibility of passing additional context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_publishers"] = models.Publisher.objects.all()
        logger.info(f"{self.__class__} --> {self.queryset}")
        return context


class BookListView(ListView):
    queryset = models.Book.objects.order_by("-publication_date")
    context_object_name = "book_list"
    template_name = 'blog/books.html'


class AcmeBookListView(ListView):
    context_object_name = "book_list"
    queryset = models.Book.objects.filter(publisher__name="ACME Publishing")
    template_name = "blog/acme_list.html"


class PublisherBookListView(ListView):
    template_name = "blog/books_by_publisher.html"

    def get_queryset(self):
        logs = {
            "request": self.request,
            "queryset": self.queryset,
            "user": self.request.user,
        }
        logger.info(logs)
        self.publisher = get_object_or_404(models.Publisher, name=self.kwargs["publisher"])
        books = models.Book.objects.filter(publisher=self.publisher)
        return books

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context["publisher"] = self.publisher
        return context


class AuthorDetailView(DetailView):
    queryset = models.Author.objects.all()
    template_name = 'blog/author.html'

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from . import views


templates_patterns = [
    path('', TemplateView.as_view(template_name="blog/about.html")),
    path('base/', TemplateView.as_view(template_name="blog/base.html"))

]

tests_patterns = [
    path('01/', views.Test01.as_view(), name='test_01'),
    path('02/', views.Test02.as_view(), name='test_02'),
    path('markdown', views.MarkdownView.as_view(), name='markdown'),

]

greetings_patterns = [
    path('1/', views.GreetingView.as_view(), name='greeting_1'),
    path('2/', views.GreetingChildView.as_view(), name='greeting_2'),
    path('3/', views.GreetingChildView.as_view(greeting="G'day"), name='greeting_3'),

]

publishers_patterns = [
    path('', views.PublisherListView.as_view()),
    path('<int:pk>/', views.PublisherDetailView.as_view()),

]

books_patterns = [
    path('', views.BookListView.as_view()),
    path('acme/', views.AcmeBookListView.as_view()),
    path("<publisher>/", views.PublisherBookListView.as_view()),

]

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('name/<first_name>/<last_name>', views.NameView.as_view(), name='name'),
    path("counter/<int:pk>/", views.ArticleCounterRedirectView.as_view(), name="article-counter"),
    path("details/<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("go-to-django/", RedirectView.as_view(url="https://www.djangoproject.com/"), name="go-to-django"),
    path('publishers-2/<int:pk>/', views.PublisherTwoDetailView.as_view()),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path('templates/', include(templates_patterns)),
    path('tests/', include(tests_patterns)),
    path('greetings/', include(greetings_patterns)),
    path('publishers/', include(publishers_patterns)),
    path('books/', include(books_patterns)),

]

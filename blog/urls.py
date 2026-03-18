from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('template/', TemplateView.as_view(template_name="blog/about.html")),
    path('name/<first_name>/<last_name>', views.NameView.as_view(), name='name'),
    path('test/01', views.Test01.as_view(), name='test_01'),
    path('test/02', views.Test02.as_view(), name='test_02'),
    path("counter/<int:pk>/", views.ArticleCounterRedirectView.as_view(), name="article-counter"),
    path("details/<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("go-to-django/", RedirectView.as_view(url="https://www.djangoproject.com/"), name="go-to-django"),
    path('greeting/1', views.GreetingView.as_view(), name='greeting_1'),
    path('greeting/2', views.GreetingChildView.as_view(), name='greeting_2'),
    path('greeting/3', views.GreetingChildView.as_view(greeting="G'day"), name='greeting_3'),
    path('publishers/', views.PublisherListView.as_view()),
    path('publishers/<int:pk>/', views.PublisherDetailView.as_view()),
    path('publishers-2/<int:pk>/', views.PublisherTwoDetailView.as_view()),
    path('books/', views.BookListView.as_view()),

]

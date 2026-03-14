from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('template/', TemplateView.as_view(template_name="blog/about.html") ),
    path('name/<first_name>/<last_name>', views.NameView.as_view(), name='name'),
    path('name-experiment', views.NameExperimentView.as_view(), name='name_experiment'),
]

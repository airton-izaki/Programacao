from django.shortcuts import render
from django.views.generic   import TemplateView



class DjangoView(TemplateView):
    template_name = 'app_django/django.html'





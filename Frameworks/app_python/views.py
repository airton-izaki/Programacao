from django.shortcuts           import render
from django.views.generic       import TemplateView


class PythonView(TemplateView):
    template_name = 'app_python/python.html'

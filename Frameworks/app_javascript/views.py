from django.shortcuts import render
from django.views.generic       import TemplateView

class JavascriptView(TemplateView):
    template_name = 'app_javascript/javascript.html'
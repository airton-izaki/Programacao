from django.shortcuts           import render
from django.views.generic       import TemplateView


class HtmlcssView(TemplateView):
    template_name = 'app_htmlcss/htmlcss.html'


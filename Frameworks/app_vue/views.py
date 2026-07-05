from django.shortcuts import render
from django.views.generic       import TemplateView


class VueView(TemplateView):
    template_name = 'app_vue/vue.html'

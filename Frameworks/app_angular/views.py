from django.shortcuts           import render
from django.views.generic       import TemplateView


class AngularView(TemplateView):
    template_name = 'app_angular/angular.html'
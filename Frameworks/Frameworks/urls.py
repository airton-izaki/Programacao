"""
URL configuration for Frameworks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_home.views                 import HomeView
from app_htmlcss.views              import HtmlcssView
from app_javascript.views           import JavascriptView
from app_python.views               import PythonView
from app_angular.views              import AngularView
from app_vue.views                  import VueView
from app_django.views               import DjangoView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',            HomeView.as_view(),       name = 'index'),

    # HTMLCSS
    path('htmlcss/',    HtmlcssView.as_view(),    name = 'htmlcss'),

    # javascript
    path('javascript/', JavascriptView.as_view(), name = 'javascript'),

    # python
    path('python/',     PythonView.as_view(),      name = 'python'),

    # angular
    path('angular/',    AngularView.as_view(),    name = 'angular'),

    # vue
    path('vue/',        VueView.as_view(),       name = 'vue'),

    # django
    path('django/',     DjangoView.as_view(),    name = 'django'),

]

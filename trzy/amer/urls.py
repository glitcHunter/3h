"""trzy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from amer import views,models
from django.conf.urls import *

from django.views.generic import TemplateView
from amer.views import GreetingView

urlpatterns =patterns('amer.views', 
    (r'^$', 'home_page',{'model': models.Character}),
    (r'^a/(?P<id>\d+)/$', 'page_title_changer'),
    (r'^form/$', 'forms_need',  {'template_name':'search_form.html'}),
    (r'^form_test/$', 'forms_need', {'template_name':'form_test.html'}),          
    (r'^contact/$', 'contact'),
    (r'^menu_form/$', 'menu_form'),
    (r'^request_view/$','request_view',{'template_name':'request_view.html'}),
    (r'^about/$', 'about',{'template_name':'about.html'}),
    url(r'^TemplateView/$', GreetingView.as_view(greeting="Good day")),
    (r'^login/$','login_view'),
    (r'^auth/$','auth_view'),
    (r'^logout/$','logout'),   
    (r'^loggedin/$','loggedin'),   
    (r'^invalid/$','invalid'),      
)

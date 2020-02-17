# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [      
    url(r'list/(?P<page>\d*)?$', views.list, name='list'),
    url(r'search/(?P<page>\d*)?$', views.search, name='search'),
    
    
    url(r'', views.index, name='index'),   #必须放在最后
    
]

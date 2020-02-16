# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [      
    url(r'data/list/(?P<page>\d*)?$', views.data_list, name='data_list'),
    url(r'', views.index, name='index'),   #必须放在最后
]

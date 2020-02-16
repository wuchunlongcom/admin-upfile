# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from .models import Files
from myAPI.pageAPI import djangoPage, PAGE_NUM

# http://localhost:8000/
#@login_required
def index(request):           
    meg = '最简单代码，实现zip、doc、excel 文件上传、下载。 <br>登录Admin后台, 上传文件并在前台显示图像。<br>\
        用户名/密码： admin/admin'
    return render(request, 'account/index.html', context=locals()) 

# 显示 http://localhost:8000/data/list/
def data_list(request, page):
    data_list = Files.objects.all().order_by('-id') 
    data_list, pageList, num_pages, page = djangoPage(data_list, page, PAGE_NUM)
    offset = PAGE_NUM * (page - 1)
    return render(request,'account/data_list.html', context=locals())   
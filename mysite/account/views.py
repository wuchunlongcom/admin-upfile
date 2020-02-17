# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, HttpResponseRedirect
from .models import Files
from myAPI.pageAPI import djangoPage, PAGE_NUM
from myAPI.fileAPI import ExtDown


# http://localhost:8000/
#@login_required
def index(request):           
    meg = '最简单代码，实现 %s 文件上传、下载。 <br>\
        登录Admin后台, 上传文件; 在前台显示、下载。<br>\
        用户名/密码： admin/admin' %ExtDown
    return render(request, 'account/index.html', context=locals()) 

# 显示 http://localhost:8000/list/
def list(request, page):
    modes = Files.objects.all().order_by('-id') 
    return data_show(request, '', modes, 1, PAGE_NUM)

# 搜索 http://localhost:8000/search/
def search(request, page):
    mode_obj = Files.objects
    modes = mode_obj.filter()

    if request.method == 'POST':
        cleanData = request.POST.dict()
        dict.pop(cleanData, 'csrfmiddlewaretoken') #删除字典中的键'csrfmiddlewaretoken'和值
        page = 1
    else:
        cleanData = request.GET.dict()
        
    if cleanData.get('q', ''):
        modes = mode_obj.filter(path__icontains=cleanData['q'])   
                
    queryString = '?'+'&'.join(['%s=%s' % (k,v) for k,v in cleanData.items()])    
    return data_show(request, queryString, modes, page, PAGE_NUM) 

def data_show(request, queryString, modes, page, PAGE_NUM):    
    data_list, pageList, num_pages, page = djangoPage(modes, page, PAGE_NUM)  #调用分页函数
    offset = PAGE_NUM * (page - 1)    
    return  render(request, 'account/data_list.html', context=locals()) 
     
# -*- coding: utf-8 -*-
import os
from django.contrib import admin
from .models import  Files
from django.contrib import messages
from myAPI.fileAPI import ExtDown


FILE_SIZE = 1024*1024*500 # 设定上传文件大小500M

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
        
    list_display = ('id','name','path')
     
    def save_model(self, request, obj, form, change):
        
        ext = os.path.splitext(obj.path.name)[1]
        
        if obj.path and obj.path.size > FILE_SIZE:
            # 文件大小大于设定值 
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'The upfile\'s too large. \
            It\'s supposed smaller than %sM.' %str(FILE_SIZE/1024/1024))
            
        elif ext not in ExtDown:
            # 文件类型不在设定范围
            messages.set_level(request, messages.ERROR)
            messages.error(request, '%s类型错误！支持文件类型：%s' %(ext, ExtDown))
            
        else:
            obj.save()

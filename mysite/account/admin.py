# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import  Files

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):    
    list_display = ('id','name','path')
   
  

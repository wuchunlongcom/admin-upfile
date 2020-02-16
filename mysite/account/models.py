# -*- coding: utf-8 -*-
from django.db import models
    
# 上传图片  设置media以显示图片
class Files(models.Model):
    name = models.CharField('文件名称', max_length=40)
    path = models.FileField(verbose_name='文件路径', upload_to="upfile/", 
                            help_text='只能是 zip 文件')
    
    def __str__(self):
        return self.name

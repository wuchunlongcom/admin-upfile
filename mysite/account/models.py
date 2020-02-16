# -*- coding: utf-8 -*-
import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings

    
# 上传文件  设置files以显示图片
class Files(models.Model):
    name = models.CharField('文件名称', max_length=40)
    path = models.FileField(verbose_name='文件路径', upload_to="upfile/", 
                            help_text='仅支持文件: zip、doc、excel ')
    
    def __str__(self):
        return self.name

@receiver(post_delete, sender=Files)
def delete_upload_files(sender, instance, **kwargs):   
    """
    admin 删除数据库记录，同时也删除文件
    """
    files = getattr(instance, 'path', '')
    if not files:
        return 
    fname = os.path.join(settings.MEDIA_ROOT, str(files))
    if os.path.isfile(fname):
        os.remove(fname)
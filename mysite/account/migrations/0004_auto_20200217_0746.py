# Generated by Django 2.2.6 on 2020-02-16 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200216_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='path',
            field=models.FileField(help_text='仅支持文件: zip、doc、excel ', upload_to='upfile/', verbose_name='文件路径'),
        ),
    ]
from django.db import models

# 首先安装pip install django-ckeditor
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    btitle = models.CharField(max_length=20)
    bcontent = RichTextUploadingField()

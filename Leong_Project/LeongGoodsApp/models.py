from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime


# Create your models here.

class TypeInfo(models.Model):
    """商品分类"""

    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    """所有商品详情"""
    gtitle = models.CharField(max_length=23)  # 商品
    # gpic = models.ImageField(upload_to='static/media') # 图片
    isDelete = models.BooleanField(default=False)  # 删除
    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 价格

    gtype = models.ForeignKey(TypeInfo)  # 商品分类的外键关系

    gclick = models.IntegerField(default=0) # 点击量
    gunit = models.CharField(max_length=20, default='500g') # 商品重量
    gjianjie = models.TextField()
    gpub_date = models.DateTimeField(datetime.datetime.now()) #　时间
    gpubj_date = models.DateTimeField() # 时间
    gpic = RichTextUploadingField()

    def __str__(self):
        return self.gtitle

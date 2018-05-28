from django.db import models


# Create your models here.

# 创造用户注册所需的数据类型
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 姓名
    upwd = models.CharField(max_length=40)  # 密码
    uemail = models.CharField(max_length=30)  # 邮箱
    uaddress = models.CharField(max_length=100)  # 地址
    uphone = models.CharField(max_length=11)  # 手机
    ureceive = models.CharField(max_length=20)  # 收件人
    uzip_code = models.CharField(max_length=6)  # 邮编
    ugender = models.BooleanField(default=False)

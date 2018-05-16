from django.db import models


# Create your models here.
class uploadModels(models.Model):
    pic = models.ImageField(upload_to='/static/media')

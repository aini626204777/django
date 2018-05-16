from django.shortcuts import render

from . import models


# Create your views here.


def index(request):
    a = models.Blog.objects.all()
    return render(request, 'index.html', {'a': a})

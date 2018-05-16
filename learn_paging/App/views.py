from django.shortcuts import render
from . import models
# Create your views here.
from django.core.paginator import  Paginator

def heroList(request, receive_id):
    list = models.HeroInfo.objects.all()
    p = Paginator(list, 5)
    page = p.page(int(receive_id))
    context = {'page': page}
    return render(request, 'herolist.html', context)
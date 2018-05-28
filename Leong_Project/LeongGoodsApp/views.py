from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    pic = models.GoodsInfo.objects.filter(gtype_id=3)
    pi2 = models.GoodsInfo.objects.filter(gtype_id=4)
    content = {'pic': pic[:4], 'pic2': pi2}
    return render(request, 'index.html', content)


def list(request,gtype_id,paging_id):
    pic = models.GoodsInfo.objects.filter(gtype_id=gtype_id)
    pp = Paginator(pic,5)
    p = pp.page(int(paging_id))
    return render(request, 'list.html',{'gtype_id':gtype_id,'p':p})

def detail(request,id):
    a = models.GoodsInfo.objects.filter(id=id)
    return render(request,'detail.html',{'a':a})

def cart(request):
    return render(request,'cart.html')
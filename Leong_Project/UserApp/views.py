from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


# Create your views here.
def register(request):
    return render(request, 'register.html')


def register_handle(request):
    uname1 = request.POST['user_name']
    upwd = request.POST['pwd']
    upwd2 = request.POST['cpwd']
    uemail1 = request.POST['email']

    try:
        uname = models.UserInfo.objects.get(uname=uname1)
        uemail = models.UserInfo.objects.get(uemail=uemail1)
        return HttpResponse('当前账号已经注册')
    except:
        if upwd == upwd2:
            user = models.UserInfo()
            user.uname = uname1
            user.upwd = upwd
            user.uemail = uemail1
            user.save()
            return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')


def loginhandle(request):
    uname = request.POST['username']
    upwd = request.POST['pwd']

    try:
        uname1 = models.UserInfo.objects.get(uname=uname)
        if upwd == uname1.upwd:
            return render(request, 'index.html')
    except:
        return HttpResponse('你的账号或者密码错误，请重新输入')

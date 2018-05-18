from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
    else:
        uname = '未登录'
    return render(request, 'index.html', {'uname': uname})


def login(request):
    return render(request, 'login.html')


def loginhandle(request):
    request.session['uname'] = request.POST['uname']
    return redirect('main:index')


def logout(request):
    del request.session['uname']
    return redirect('main:index')

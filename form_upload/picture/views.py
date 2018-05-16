from django.shortcuts import render
from django.http import HttpResponse
import os
from form_upload import settings


# Create your views here.

def uploadPic(request):
    return render(request, 'uploadPic.html')


def uploadHandle(request):
    pic1 = request.FILES.get('pic1')

    # 构建文件路劲
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)

    with open(picName, 'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return render(request,'uploadHandle.html',{'pic1':pic1.name})

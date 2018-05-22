from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


def getHandle(request):
    a = request.GET.get('key1')
    b = request.GET.get('key2')
    c = int(a)+int(b)
    return JsonResponse({'c':c})

@csrf_exempt
def postHandle(request):
    a = request.POST.get('key1')
    b = request.POST.get('key2')
    print(a,b)
    return JsonResponse({'u':b})

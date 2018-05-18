from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^login/',views.login,name='login'),
    url(r'^loginhandle',views.loginhandle,name='loginhandle'),
    url(r'^logout/',views.logout,name='logout')
]
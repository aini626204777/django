from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^list/(?P<gtype_id>[\d]+)/(?P<paging_id>[\d+]+)/$',views.list,name='list'),
    url(r'^detail/(?P<id>[\d]+)/$',views.detail,name='detail'),
    url(r'^cart/',views.cart,name='cart'),
]


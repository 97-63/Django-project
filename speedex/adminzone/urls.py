from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.adminhome,name='adminhome'),
    url(r'^$',views.logout,name='logout'),
    url(r'^$',views.adminhome,name='adminhome'),
    url(r'^addnotification',views.addnotification,name='addnotification'),
    url(r'^city',views.city,name='city'),
    url(r'^cities',views.cities,name='cities'),
    url(r'^delete/(?P<id>\d+)$',views.delete,name='delete'),
    url(r'^packet',views.packet,name='packet'),
    url(r'^calling',views.calling,name='calling'),
    url(r'^packupdel',views.packupdel,name='packupdel'),
    url(r'^delete3/(?P<refno>\w+)$',views.delete3,name='delete3'),
    url(r'^delete1/(?P<id>\d+)$',views.delete1,name='delete1'),
    url(r'^quali',views.quali,name='quali'),
    url(r'^seequalification',views.seequalification,name='seequalification'),
    url(r'^qualification',views.qualification,name='qualification'),
    url(r'^delete2/(?P<id>\d+)$',views.delete2,name='delete2'),
    url(r'^upack', views.upack, name='upack'),
    url(r'^update/(?P<refno>\w+)$',views.update,name='update'),
    url(r'^careermanagement',views.careermanagement,name="careermanagement"),
    url(r'^delete4/(?P<id>\d+)$',views.delete4,name='delete4'),
    url(r'^managecomplain', views.managecomplain, name='managecomplain'),
    url(r'^delete5/(?P<contactno>\d+)$',views.delete5,name='delete5'),
]
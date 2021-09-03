from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('',homepage,name='homepage'),
    path('loginUser/',LoginUser,name='loginUser'),
    path('dashboard/',Login,name='dashboard'),
    path('dashboardHome/',dashboardHome,name='dashboardHome'),
    path('addUser/',AddUser,name='addUser'),
    path('storeUser/',storeUser,name='storeUser'),
    path('markAttendence/',markAttendence,name='markAttendence'),
    path('markLeave/',markLeave,name='markLeave'),
    path('markLeaveReq/',markLeaveReq,name='markLeaveReq'),
    path('leaveReq/',leaveReq,name='leaveReq'),
    path('viewAttendence/',viewAttendence,name='viewAttendence'),
    path('Logout/',Logout,name='Logout'),
    path('changeProfile/',changeProfile,name='changeProfile'),
    path('UpdateProfile/',UpdateProfile,name='UpdateProfile'),
]
from django.conf import settings
from django.conf.urls.static import static
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
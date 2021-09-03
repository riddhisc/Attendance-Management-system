from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('',homepage),
    path('LoginAdmin/',LoginAdmin,name='LoginAdmin'),
    path('AdminDash/',AdminDash,name='AdminDash'),
    path('AdminDashHome/',AdminDashHome,name='AdminDashHome'),
    path('Students/',Students,name='Students'),
    path('delStudent/<str:reg>',delStudent,name='delStudent'),
    path('AdminviewAttendence/',AdminviewAttendence,name='AdminviewAttendence'),
    path('openAttendence/<str:att_id>',openAttendence,name='openAttendence'),
    path('editAttendence/<str:att_id>',editAttendence,name='editAttendence'),
    path('updateAttendence/<str:att_id>',updateAttendence,name='updateAttendence'),
    path('delAttendence/<str:att_id>',delAttendence,name='delAttendence'),
    path('newAttendence/',newAttendence,name='newAttendence'),
    path('addNewAttendence/',addNewAttendence,name='addNewAttendence'),
    path('LeaveRequestShow/',LeaveRequestShow,name='LeaveRequestShow'),
    path('approveLeave/<str:leave_req>',approveLeave,name='approveLeave'),
    path('NapproveLeave/<str:leave_req>',NapproveLeave,name='NapproveLeave'),
    path('reportInput/',reportInput,name='reportInput'),
    path('ShowReport/',ShowReport,name='ShowReport'),
    path('grade/',grade,name='grade'),
    path('AdminLogout/',AdminLogout,name='AdminLogout'),
]
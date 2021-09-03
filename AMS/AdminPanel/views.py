from UserPanel.models import Student
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .models import *
from UserPanel.models import *
import datetime

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def LoginAdmin(request):
    return render(request,'admin/Adminlogin.html')

def AdminDash(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if(Admin.objects.filter(admin_username=username,admin_password=password).exists()):
        students=Student.objects.all().count()
        leave_req=LeaveRequest.objects.filter(req_status='Pending').count()
        att_per=Attendence.objects.filter(att_status='Present').count()/Attendence.objects.all().count()
        att_per=att_per*100
        
        print(students)
        print(leave_req)
        print(att_per)
        return render(request,'admin/adminHome.html',{'Students':students,'LeaveReq':leave_req,'Att_Per':att_per})
    else:
        messages.error(request, f"Incorrect Password or Username! Please Try Again")
        return redirect('/adminLogin')
    
def AdminDashHome(request):
    students=Student.objects.all().count()
    leave_req=LeaveRequest.objects.filter(req_status='Pending').count()
    att_per=Attendence.objects.filter(att_status='Present').count()/Attendence.objects.all().count()
    att_per=att_per*100
    
    print(students)
    print(leave_req)
    print(att_per)
    return render(request,'admin/adminHome.html',{'Students':students,'LeaveReq':leave_req,'Att_Per':att_per})
    
    # return render(request,'admin/adminHome.html')

def Students(request):
    students=Student.objects.all()
    return render(request,'admin/Students.html',{'Students':students})
    
def AdminviewAttendence(request):
    att=Attendence.objects.all()
    return render(request,'admin/viewAttendence.html',{'Attendence':att})
    # return render(request,'admin/viewAttendence.html')

def openAttendence(request,att_id):
    att=Attendence.objects.get(att_id=att_id)
    reg=att.std_reg_id
    std=Student.objects.get(std_reg=reg)
    return render(request,'admin/openAttendence.html',{'student':std,'attendence':att})

def editAttendence(request,att_id):
    att=Attendence.objects.get(att_id=att_id)
    reg=att.std_reg_id
    std=Student.objects.get(std_reg=reg)
    return render(request,'admin/editAttendence.html',{'student':std,'attendence':att})
        
def updateAttendence(request,att_id):
    status=request.POST.get('status')
    print(att_id)
    
    att=Attendence.objects.get(att_id=att_id)
    std=Student.objects.get(std_reg=att.std_reg_id)
    att.att_status=status
    att.save()
    messages.info(request,f"Attendece Changed Successfully!")
    return render(request,'admin/openAttendence.html',{'student':std,'attendence':att})

def delAttendence(request,att_id):
    att=Attendence.objects.get(att_id=att_id)
    att.delete()
    messages.success(request, "Attendence Deleted Successfully")
    att=Attendence.objects.all()
    return redirect('AdminviewAttendence')

def newAttendence(request):
    std=Student.objects.all()
    return render(request,'admin/newAttendence.html',{'students':std})

def addNewAttendence(request):
    
    reg=request.POST.get('reg')
    date=datetime.datetime.today().strftime('%Y-%m-%d')
    if (Attendence.objects.filter(std_reg=reg,att_date=date).exists()):
        obj=Attendence.objects.get(std_reg=reg,att_date=date)
        messages.success(request, "Attendence Already Marked!")
    else:
        status=request.POST.get('status')
        att=Attendence()
        att.std_reg=Student.objects.get(std_reg=reg)
        att.att_status=status
        att.save()
        messages.success(request, "Attendence Marked Successfully")
    return redirect('AdminviewAttendence')

def delStudent(request,reg):
    std=Student.objects.get(std_reg=reg)
    std.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('Students')
    
def LeaveRequestShow(request):
    reqs=LeaveRequest.objects.all()
    # print(reqs)
    return render(request,'admin/LeaveRequest.html', {'Request': reqs})


def approveLeave(request,leave_req):
    req=LeaveRequest.objects.get(req_id=leave_req)
    req.req_status='Approved'
    req.save()
    
    reg=req.std_reg_id
    date=req.req_date
    att=Attendence.objects.get(std_reg_id=reg,att_date=date)
    att.att_status='Leave'
    att.save()
    
    
    return redirect('LeaveRequestShow')

def NapproveLeave(request,leave_req):
    req=LeaveRequest.objects.get(req_id=leave_req)
    req.req_status='Not Approved'
    req.save()
    
    reg=req.std_reg_id
    date=req.req_date
    att=Attendence.objects.get(std_reg_id=reg,att_date=date)
    att.att_status='Absent'
    att.save()
    
    return redirect('LeaveRequestShow')

def reportInput(request):
    stds=Student.objects.all()
    return render(request,'admin/reportInput.html',{'Students':stds})

def ShowReport(request):
    from_date=request.POST.get('from')
    to_date=request.POST.get('to')
    reg=request.POST.get('reg')
    
    
    att=Attendence.objects.filter(att_date__gte=from_date, att_date__lte=to_date,std_reg=reg)
    
    print(from_date)
    print(to_date)
    print(reg)
    print(att)
    
    # att=Attendence.objects.filter()
    return render(request,'admin/ShowReport.html',{'attendence':att})

def grade(request):
    stds=Student.objects.all()
    reg=request.POST.get('reg') 
    print(reg)
    if(reg is not None): 
        presents=Attendence.objects.filter(std_reg=reg,att_status='Present').count()
        absents=Attendence.objects.filter(std_reg=reg,att_status='Absent').count()
        leaves=Attendence.objects.filter(std_reg=reg,att_status='Leave').count()
        grade=presents/(presents+absents+leaves)
        
        grade=grade*100
        print(grade)
        if(grade<50):
            grade='C'
        elif(grade>=50 and grade<=60):
            grade='B'
        elif(grade>60 and grade<=80):
            grade='A'
        elif(grade>80 ):
            grade='A+'
        
        print('Grade',grade)
        return render(request,'admin/grade.html',{'Grade':grade,'Presents':presents,'Leaves':leaves,'Absents':absents,'Students':stds})
    else:
        return render(request,'admin/grade.html',{'Students':stds})

def AdminLogout(request):
    return redirect('LoginAdmin')



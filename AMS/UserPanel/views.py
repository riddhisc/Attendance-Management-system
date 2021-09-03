from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import datetime

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def LoginUser(request):
    return render(request,'user/login.html')

def Login(request):
    reg=request.POST.get('registration')
    password=request.POST.get('password')
    print(reg)
    print(password)
    if(Student.objects.filter(std_reg=reg)).exists():
        obj=Student.objects.get(std_reg=reg)
        if(obj.std_password==password):
            request.session['registration'] = reg
            obj=Student.objects.get(std_reg=reg)
            presents=Attendence.objects.filter(std_reg=reg,att_status='Present').count()
            absents=Attendence.objects.filter(std_reg=reg,att_status='Absent').count()
            leaves=Attendence.objects.filter(std_reg=reg,att_status='Leave').count()
            return render(request,'user/attendence.html',{'student':obj,'presents':presents,'leaves':leaves,'absents':absents})
        else:
            messages.error(request, f"Incorrect Password! Please Try Again")
            return redirect('/loginUser')
    else:
        messages.error(request, f"Record Dosen't Exist")
        return redirect('/loginUser')
        
def dashboardHome(request):
    reg=request.session['registration'] 
    obj=Student.objects.get(std_reg=reg)
    presents=Attendence.objects.filter(std_reg=reg,att_status='Present').count()
    absents=Attendence.objects.filter(std_reg=reg,att_status='Absent').count()
    leaves=Attendence.objects.filter(std_reg=reg,att_status='Leave').count()
    return render(request,'user/attendence.html',{'student':obj,'presents':presents,'leaves':leaves,'absents':absents})
              
def AddUser(request):
    return render(request,'user/signup.html')



def storeUser(request):
    print('Im in StoreUSer')
    if(Student.objects.filter(std_cnic=request.POST.get('cnic'))).exists():
        # objects already present
        messages.warning(request, f"User Already Registered!")
    else:
        std=Student()
        
        std.std_name=request.POST.get('name')
        std.std_email=request.POST.get('email')
        std.std_cnic=request.POST.get('cnic')
        std.std_password=request.POST.get('password')
        
        
        
        # Creating registration number
        # get the first alphabets of name
        name=std.std_name
        name=name.split(' ')
        alpha=''
        for words in name:
            alpha+=words[0]
        
        # registration=current year last 2 digits + name first character + lasat digit of cnic
        std.std_reg=str(datetime.datetime.now().year)[2:]+alpha+str(std.std_cnic)[-1]
    
        # save new objects
        # std.save()
        image = request.FILES['image'] 
        std.std_image.save(image.name,image,)
        print('save successs')
        messages.success(request, f"Registration Succesfully Done! \n Your Registration Number is {std.std_reg}")
        
        
    return redirect('/loginUser')
        
def markAttendence(request):
    reg=request.session['registration'] 
    # date = datetime.datetime.now()
    # date = date.strftime("%B %d,%Y")
    obj2=Student.objects.get(std_reg=reg)
    date=datetime.datetime.today().strftime('%Y-%m-%d')
    if (Attendence.objects.filter(std_reg=reg,att_date=date).exists()):
        obj=Attendence.objects.get(std_reg=reg,att_date=date)
        msg='Your Attendence Already Marked!'
        return render(request,'user/markattendence.html',{'MSG':msg,'OBJ':obj,'student':obj2})
    else:
        att=Attendence()
        att.std_reg=Student.objects.get(std_reg=reg)
        att.att_status='Present'
        att.save()
        obj=Attendence.objects.get(std_reg=reg,att_date=date)
        msg='Your Attendence  Marked SuccessFully!'
        return render(request,'user/markattendence.html',{'MSG':msg,'OBJ':obj,'student':obj2})

def markLeave(request):
    reg=request.session['registration'] 
    # date = datetime.datetime.now()
    # date = date.strftime("%B %d,%Y")
    obj2=Student.objects.get(std_reg=reg)
    date=datetime.datetime.today().strftime('%Y-%m-%d')
    if (Attendence.objects.filter(std_reg=reg,att_date=date).exists()):
        obj=Attendence.objects.get(std_reg=reg,att_date=date)
        msg='Your Attendence Already Marked!'
        return render(request,'user/markattendence.html',{'MSG':msg,'OBJ':obj,'student':obj2})
    else:
        att=Attendence()
        att.std_reg=Student.objects.get(std_reg=reg)
        att.att_status='Absent'
        att.save()
        obj=Attendence.objects.get(std_reg=reg,att_date=date)
        msg='Your Leave Marked SuccessFully!'
        return render(request,'user/markattendence.html',{'MSG':msg,'OBJ':obj,'student':obj2})
    
def markLeaveReq(request):
    reg=request.session['registration'] 
    obj=Student.objects.get(std_reg=reg)
    return render(request,'user/markLeaveReq.html',{'student':obj})
    
def leaveReq(request):
    reg=request.session['registration'] 
    obj2=Student.objects.get(std_reg=reg)
    date=datetime.datetime.today().strftime('%Y-%m-%d')
    if (Attendence.objects.filter(std_reg=reg,att_date=date).exists()):
        obj=Attendence.objects.get(std_reg=reg,att_date=date)
        msg='Your Attendence Already Marked!'
        return render(request,'user/markattendence.html',{'MSG':msg,'OBJ':obj,'student':obj2})
    else:
        # mark temporary leave
        att=Attendence()
        att.std_reg=Student.objects.get(std_reg=reg)
        att.att_status='Leave'
        att.save()
        
        # save leave to approve
        leave=LeaveRequest()
        leave.std_reg=Student.objects.get(std_reg=reg)
        leave.req_reason=request.POST.get('reason')
        leave.save()
        
        obj=Attendence.objects.get(std_reg=reg,att_date=date)
        msg='Your Leave Request Submitted SuccessFully!'
        return render(request,'user/markattendence.html',{'MSG':msg,'OBJ':obj,'student':obj2})
    
def viewAttendence(request):
    reg=request.session['registration'] 
    attendence=Attendence.objects.filter(std_reg=reg)
    obj2=Student.objects.get(std_reg=reg)
    return render(request,'user/viewAttendence.html',{'student':obj2,'attendence':attendence})

def Logout(request):

    del request.session['registration']
    messages.error(request, f"You're logged out")
    return redirect('/loginUser')

def changeProfile(request):
    reg=request.session['registration'] 
    std=Student.objects.get(std_reg=reg)
    return render(request,'user/changeProfile.html',{'student':std})


def UpdateProfile(request):
    reg=request.session['registration'] 
    std=Student.objects.get(std_reg=reg)
    image = request.FILES['image'] 
    std.std_image.save(image.name,image,)
    std.save()
    return render(request,'user/changeProfile.html',{'student':std})
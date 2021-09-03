from django.db import models

# Create your models here.
class Student(models.Model):
    std_reg=models.CharField(max_length=5,primary_key=True)
    std_name=models.CharField(max_length=150,blank=False)
    std_email=models.EmailField(blank=False)
    std_password=models.CharField(max_length=20)
    std_cnic=models.CharField(max_length=150,unique=True)
    std_image=models.ImageField(upload_to='upload/',blank=False)
    
    def __str__(self):
        return str(self.std_name)


class LeaveRequest(models.Model):
    req_status_option=(('A','Approved'),('P','Pending'),('N','Not Approved'))
    req_id= models.AutoField(primary_key=True)
    std_reg=models.ForeignKey('Student',on_delete = models.CASCADE)
    req_reason=models.TextField()
    req_date=models.DateField(auto_now_add=True)
    req_time=models.TimeField(auto_now_add=True)
    req_status=models.CharField(max_length=1,choices=req_status_option,default='Pending')
    
    
class Attendence(models.Model):
    status_option=(('A','Absent'),('P','Present'),('L','Leave'))
    att_id=models.AutoField(primary_key=True)
    std_reg=models.ForeignKey('Student',on_delete = models.CASCADE)
    att_date=models.DateField(auto_now_add=True)
    att_time=models.TimeField(auto_now_add=True)
    att_status=models.CharField(max_length=1,choices=status_option)
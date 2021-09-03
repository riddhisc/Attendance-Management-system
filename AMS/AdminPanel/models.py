from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_id= models.AutoField(primary_key=True)
    admin_username= models.CharField(max_length=20)
    admin_password= models.CharField(max_length=20)
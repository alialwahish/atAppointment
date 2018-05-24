from django.db import models
import datetime




class  Users(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=32)
    dob=models.DateField()
    gender=models.CharField(max_length=5)
    is_manager=models.BooleanField()
    is_staff=models.BooleanField()
    is_customer=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Appointments(models.Model):
    customer=models.ForeignKey(Users,null=True ,on_delete=models.CASCADE,related_name='appointments')
    staff_user=models.ForeignKey(Users,null=True ,on_delete=models.CASCADE,related_name='staff_user')
    appointment_time=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# class Join(models.Model):
#         staff_user=models.OneToOneField(Appointments,on_delete=models.CASCADE)

#   from apps.atApt.models import *
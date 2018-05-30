from django.db import models
from django.db import models
from django.contrib import messages
from django.contrib.messages import get_messages
import datetime

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-copyZ0-9._-]+\.[a-zA-Z]+$')
from passlib.hash import sha256_crypt



class userManager(models.Manager):
    def customer_register(self,request):
        print("in customer register")
        if len(request.POST["name"]) < 3:
            messages.add_message( request, messages.ERROR, "Name Can't be less than 3 characters!" )
      
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.add_message(request,messages.ERROR,"please use valid Email address")

        if len(request.POST["password"]) < 8:
            messages.add_message( request, messages.ERROR, "Password must be between 8-32 characters!" )
        if request.POST["password"] != request.POST["confirm_password"]:
            messages.add_message( request, messages.ERROR, "Password and Password Confirmation must match!" )

        today=datetime.date.today()
        if(request.POST["dob"] > str(today)):
            messages.add_message( request, messages.ERROR, "Date of birth Can't in the future!" )
       
        if len(request.POST["dob"]) < 1:
            messages.add_message( request, messages.ERROR, "Date of birth Can't be Empty!" )


        if Users.objects.filter(email=request.POST["email"]).count() > 0:
            messages.add_message( request, messages.ERROR, "A user with this email already exists!" )

        if len( get_messages(request) ) > 0:
            return False
        else:
            Users.objects.create(
            name = request.POST["name"],email = request.POST["email"],password = sha256_crypt.hash(request.POST['password']),dob=request.POST['dob'],is_manager=False,is_staff=False,is_customer=True)

            return True




    def staff_register(self,request):
        print("got to models to validate the staff")
        if len(request.POST["name"]) < 3:
            messages.add_message( request, messages.ERROR, "Name Can't be less than 3 characters!" )
      
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.add_message(request,messages.ERROR,"please use valid Email address")

        if len(request.POST["password"]) < 8:
            messages.add_message( request, messages.ERROR, "Password must be between 8-32 characters!" )
        if request.POST["password"] != request.POST["confirm_password"]:
            messages.add_message( request, messages.ERROR, "Password and Password Confirmation must match!" )

        today=datetime.date.today()
        if(request.POST["dob"] > str(today)):
            messages.add_message( request, messages.ERROR, "Date of birth Can't in the future!" )
       
        if len(request.POST["dob"]) < 1:
            messages.add_message( request, messages.ERROR, "Date of birth Can't be Empty!" )


        if Users.objects.filter(email=request.POST["email"]).count() > 0:
            messages.add_message( request, messages.ERROR, "A user with this email already exists!" )

        if len( get_messages(request) ) > 0:
            return False
            
        else:
            Users.objects.create(
            name = request.POST["name"],email = request.POST["email"],password = sha256_crypt.hash(request.POST['password']),dob=request.POST['dob'],is_manager=False,is_staff=True,is_customer=False)

            return True





    def login(self,request):
        print('login user')
        try:
            print(request.POST['email'])
            
            user = Users.objects.get(email=request.POST['email'])
            print(user.email)
                       
            if sha256_crypt.verify(request.POST['password'], user.password):
                request.session['logged']=user.id

                print("Password match")
          
                return True
            else:
                
                messages.add_message( request, messages.ERROR, "Wrong Password!" )
                return False        
        
        except:
            messages.add_message( request, messages.ERROR, "User doesn't exist!" )
            return False




class  Users(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=32)
    dob=models.DateField()
    is_manager=models.BooleanField()
    is_staff=models.BooleanField()
    is_customer=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=userManager()

class AppointmentsManager(models.Manager):
    def add_appointment(self,request):
        id=request.session['logged']
        user=Users.objects.get(id=id)
        today=str(datetime.date.today())
        customer=Users.objects.get(id=request.session['logged'])
        print("Coming from post for staff",request.POST['staff'])
        staff_user=Users.objects.get(id=request.POST['staff'])
        print(staff_user.name)
        print(request.POST["time"])
        time=request.POST["time"]
        date=request.POST["date"]
        print("accepted time!")




        if date<today:
            messages.add_message( request, messages.ERROR, "Appointment can't be in the past!" )
            return False
        else:
            print("adding appointment")
            Appointments.objects.create(customer=customer,appointment_time=time,staff_user=staff_user,appointment_date=date)
            print("user created!")
            return True
    
    
    def delete_appointment(self,request,apt_id):
        Appointments.objects.get(id=apt_id).delete()

    def staff_delete_first(self,request):
        Appointments.objects.first().delete()
        

class Appointments(models.Model):
    customer=models.ForeignKey(Users,null=True ,on_delete=models.CASCADE,related_name='appointments')
    staff_user=models.ForeignKey(Users,null=True ,on_delete=models.CASCADE,related_name='staff_user')
    appointment_time=models.CharField(max_length=255)
    appointment_date = models.CharField(max_length=255)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=AppointmentsManager()
    
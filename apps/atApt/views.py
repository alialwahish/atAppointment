from django.shortcuts import render,redirect
from .models import Users,Appointments
from django.contrib import messages



def index(request):

    return redirect('/main')



def main(request):
    print("home page")
    
    return False
    # return render(request,'{{main-view}}/index.html')

def user_page(request):
    id=request.session['logged']
    user=Users.objects.get(id=id)
    # return render(request,'{{user-page-view}}/index.html')

    return False


def staff_register(request):
    print ("registering staff")
    if  Users.objects.staff_register(request):
        print ('staff created')
        messages.add_message(request,messages.INFO,"Staff Added")
        return redirect('/main')
    else:
        return redirect('/main')



def customer_register(request):
    print ("registering customer")
    if  Users.objects.customer_register(request):
        print ('customer created')
        
        messages.add_message(request,messages.INFO,"Customer Added")
        return redirect('/main')
    else:
        return redirect('/main')


    
def login(request):
    
    if(Users.objects.login(request)):
        print(request.session['logged'])
        # return redirect('/travel')
        return False
    else:
        return redirect('/main')

def logout(request):
    request.session['logged']=""
    return redirect('/main')


def add_appointment(request):
    print("adding an appointment")
    Users.objects.add_appointment(request)
    return False
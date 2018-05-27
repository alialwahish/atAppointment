from django.shortcuts import render,redirect
from .models import Users,Appointments
from django.contrib import messages



def index(request):
    print("in index")

    return redirect('/main')



def main(request):
    print("getting to home page")
    
    return render(request,'atApt/index.html')

def user_page(request):
    id=request.session['logged']
    user=Users.objects.get(id=id)
    return render(request,'atApt/add_appointment.html')






def staff_register(request):
    print ("registering staff")
    if  Users.objects.staff_register(request):
        print ('staff created')
        messages.add_message(request,messages.INFO,"Staff Added")
        return redirect('/main')
    else:
        return redirect('/main')


def registration(request):



    return render(request,'atApt/registration.html')


def customer_register(request):
    print ("registering customer")
    if  Users.objects.customer_register(request):
        print ('customer created')
        
        messages.add_message(request,messages.INFO,"Customer Added")
        return redirect('/main')
    else:
        return redirect('/main')



def customer_Dashboard(request):
    id=request.session["logged"]
    user=Users.objects.get(id=id)
    print(user.name)
    staff=Users.objects.filter(is_staff=True)
    userAppts=Appointments.objects.filter(customer=user)
    context={'user':user , 'staff':staff,'userAppts':userAppts}
    return render(request,'atApt/add_appointment.html',context)


def staff_adding(request):

    if Users.objects.staff_register(request):
        messages.add_message(request,messages.INFO,"Staff Added")
        return redirect('/admin_view')

    else:
        return redirect('/add_staff_view')




def add_staff_view(request):

    id=request.session["logged"]
    user=Users.objects.get(id=id)
    print(user.name)
    return render(request,'atApt/add_staff.html',{'user':user})







def admin_view(request):
    id=request.session["logged"]
    user=Users.objects.get(id=id)
    
    staff=Users.objects.filter(is_staff=True)
    appts=Appointments.objects.all()
    customers=Users.objects.filter(is_customer=True)
    context={'user':user , 'staff':staff,'appts':appts,'customers':customers}
    return render(request,'atApt/admin_view.html',context)



def login(request):
    
    if(Users.objects.login(request)):
        
        id=request.session["logged"]
        user=Users.objects.get(id=id)
        if user.is_manager:
            print(user.is_manager)
            print("manager access")
            return redirect('/admin_view')


        if user.is_staff:
            print(user.is_manager)
            print("manager access")
            return redirect('/staff_view')


        return redirect('/customer_Dashboard')
        
    else:
        return redirect('/main')

def staff_view(request):
    staff_id=request.session['logged']
    staff=Users.objects.get(id=staff_id)
    staff_appointments=Appointments.objects.filter(staff_user=staff)
    return render(request,'atApt/staff_view.html',{'staff':staff,'staff_appointments':staff_appointments})



def logout(request):
    request.session['logged']=""
    return redirect('/main')


def add_appointment(request):
    print("adding an appointment")
    if Appointments.objects.add_appointment(request):
        return redirect('/customer_Dashboard')
    else:
        return redirect('/customer_Dashboard')


def delete_appointment(request,id):

    Appointments.objects.delete_appointment(request,id)
    return redirect('/customer_Dashboard')

def delete_appointment_admin(request,id):

    Appointments.objects.delete_appointment(request,id)
    return redirect('/admin_view')

def delete_appointment_staff(request,id):
    Appointments.objects.delete_appointment(request,id)
    return redirect('/staff_view')


def staff_delete_first(request):
    Appointments.objects.staff_delete_first(request)
    return redirect('/staff_view')
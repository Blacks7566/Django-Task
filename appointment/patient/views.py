from django.shortcuts import render,redirect

from . models import Patient

from django.contrib import messages




# Create your views here.


def home(request):

    if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        gender = request.POST.get('gen')
        
        if mobile.isdigit():
            data = Patient(name=name,age=age,gender=gender,mobile=mobile,address=address)
            data.save()

            messages.success(request,'Appointment Scheduled Successfully..(* - *)')
        
        else:

            messages.error(request,'Enter valid mobile number.....!')
        
                    
    
     
    return render(request,'home.html')


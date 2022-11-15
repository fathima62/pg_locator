from django.shortcuts import render
from common.models import Customer
# Create your views here.

    

def property(request):
     
    return render(request,'user/property_details.html')

def property_list(request):
    return render(request,'user/property_list.html')

def request_status(request):
    return render(request,'user/request_status.html')

def user_profile(request):
    user = Customer.objects.get(id=request.session['userid'])
    return render(request,'user/user_profile.html',{"user_profile":user})





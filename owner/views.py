from django.shortcuts import render,redirect
from owner.models import Owner

# Create your views here.

def owner_login(request):
    
    if request.method == 'POST':   
              
            owner_email = request.POST['email']
            owner_password = request.POST['password']
            try:  
                owner =  Owner.objects.get(email=owner_email, password=owner_password)
                request.session['ownerid'] = owner.id
                return redirect('owner:home')
            except:
                msg = "invalid username and password"
                return render(request, 'owner/login.html',{"error_msg":msg})

    
    return render(request, 'owner/login.html')
    

    
def customer(request):
    return render(request,'owner/customer.html')

def employee(request):
    return render(request,'owner/employee.html')

def hostel_profile(request):
    return render(request,'owner/hostel_profile.html')

def leaved_employee(request):
    return render(request,'owner/leaved_employee.html')

def leaved_customer(request):
    return render(request,'owner/leaved_customer.html')

def manage_employee(request):
    return render(request,'owner/manage_room.html')

def manage_customer(request):
    return render(request,'owner/manage_customer.html')

def rooms(request):
    return render(request,'owner/manage_room.html')

def fees(request):
    return render(request,'owner/monthly_fees.html')

def new_employee(request):
    return render(request,'owner/new_employee.html')

def new_students(request):
    return render(request,'owner/new_students.html')

def owner(request):
    owner = Owner.objects.get(id=request.session['ownerid'])
    return render(request,'owner/owner_profile.html',{'owner_profile':owner})

def room_request(request):
    return render(request,'owner/room_request.html')

def salary(request):
    return render(request,'owner/salary.html')

def fees_payment(request):
    return render(request,'owner/customer_fees.html')

def home(request):
    return render(request,'owner/home.html')

def list_property(request):
    return render(request,'owner/list_property.html')

def house(request):
    return render(request,'owner/independent_house_registration.html')

def hostel(request):
    return render(request,'owner/hostel_reg.html')

def type(request):
    return render(request,'owner/property_type.html')

def profile_update(request):
    if request.method == 'POST':
           name = request.POST['full_name']
           phone = request.POST['phone']
           address = request.POST['address']
           s_image = request.FILES['photo']
           gender = request.POST['gender']
    profile = Owner.objects.filter(id = request.session['ownerid']).update(name = name,phone = phone,address = address,photo = s_image,gender = gender)
    profile.save()

def signup(request):
    
    if request.method == 'POST':
      
              owner_name = request.POST['full_name']
              owner_email = request.POST['email']
              owner_phone = request.POST['phone']
              owner_address = request.POST['address']
              s_password = request.POST['password']
              s_image = request.FILES['photo']
              gender = request.POST['gender']
              obj = Owner(name=owner_name,
                            email=owner_email,
                            phone=owner_phone,
                            address=owner_address,
                            password=s_password,
                            photo=s_image,
                            gender=gender)
              obj.save()
              return redirect ('owner:list_property')
    return render(request, 'owner/signup.html')

def logout(request):
   del request.session['ownerid']
   request.session.flush()
   return redirect('common:home')

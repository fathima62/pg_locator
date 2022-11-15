from django.shortcuts import redirect, render
from django.http import JsonResponse
from common.models import Customer


# Create your views here.

def home(request):
    if request.method == 'POST':
        if 'customer_signup' in request.POST:
            print('test')
            first_name = request.POST['first_name']
            sec_name = request.POST['second_name']
            cus_email = request.POST['email']
            cus_phone = request.POST['phone']

            cus_address = request.POST['address']
            cus_password = request.POST['password']
            cus_data = Customer(first_name=first_name,
                                second_name=sec_name,
                                c_email=cus_email,
                                c_phone=cus_phone,
                                c_address=cus_address,
                                c_password=cus_password,)
            cus_data.save()

    

        if 'c_login' in request.POST:

            customer_email = request.POST['c_email']
            customer_password = request.POST['c_password']
       
             
            try:  
                customer =  Customer.objects.get(c_email=customer_email, c_password=customer_password)
                request.session['userid'] = customer.id
                return redirect('common:home')
            except:
                msg = "invalid username and password"
                return render(request, 'common/home.html',{"error_msg":msg})


    
    # user = Customer.objects.get(id=request.session['userid']){'user_data':user}
    return render(request, 'common/home.html',)
      
  

def logout(request):
    del request.session['userid']
    request.session.flush()
    return redirect('common:home') 

def email_exist(request):
    email = request.POST['email']   
    e_exist = Customer.objects.filter(c_email= email).exists()
    return JsonResponse({'status':e_exist})









def mas(request):
    return render(request, 'common/mas.html')






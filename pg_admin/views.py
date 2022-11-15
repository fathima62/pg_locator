from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'pg_admin/login.html')

def logout(request):
    return render(request,'pg_admin/logout.html')

def contacts(request):
    return render(request,'pg_admin/contacts.html')

def new_pg_request(request):
    return render(request,'pg_admin/new_pg_request.html')

def pg(request):
    return render(request,'pg_admin/pg.html')

def user(request):
    return render(request,'pg_admin/users.html')

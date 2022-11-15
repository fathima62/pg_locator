from unicodedata import name
from django.urls import path
from . import views

app_name='owner'

urlpatterns=[
    path('owner_login',views.owner_login,name="owner_login"),
 
    path('cutomer_fees',views.fees_payment,name="customer_fees"),
    path('customer',views.customer,name="customer"),
    path('employee',views.employee,name="employee"),
    path('hostel_profile',views.hostel_profile,name="profile"),
    path('leaved_empolyee',views.leaved_employee,name="leaved_employee"),
    path('leaved_customer',views.leaved_customer,name="leaved_customer"),
    path('manage_employee',views.manage_employee,name="manage_employee"),
    path('manage_customer',views.manage_customer,name="manage_customer"),
    path('fees',views.fees,name="fees"),
    path('new_employee',views.new_employee,name="new_employee"),
    path('new_students',views.new_students,name="new_students"),
    path('profile',views.owner,name="owner_profile"),
    path('rooms',views.rooms,name="rooms"),
    path('room_request',views.room_request,name="room_request"),
    path('salary',views.salary,name="salary"),
    path('home',views.home,name="home"),
    path('list_property',views.list_property,name="list_property"),
    path('house_registration',views.house,name="house"),
     path('hostel_registration',views.hostel,name="hostel"),
    path('type',views.type,name="type"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path('update_profile',views.profile_update,name="profile_update"),
    

]
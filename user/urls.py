from django.urls import path
from . import views

app_name='user'

urlpatterns=[
   
   
    path('pgdetails',views.property,name="property"),
    path('pglist',views.property_list,name="pglist"),
    path('status',views.request_status,name="status"),
    path('profile',views.user_profile,name="profile"),
   
   
    
]
from unicodedata import name
from django.urls import path
from . import views

app_name='common'

urlpatterns=[
    path('',views.home,name="home"),
  
   
    path('mas',views.mas,name="mas"),
   
    path('logout',views.logout,name="logout"),
    path('email_exist',views.email_exist,name="email_exist"),    
]
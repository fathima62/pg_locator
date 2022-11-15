from django.urls import path

from . import views

app_name='pgadmin'

urlpatterns=[
    path('login',views.login,name="adminlogin"),
    path('logout',views.logout,name="adminlogout"),
    path('contacts',views.contacts,name="contacts"),
    path('new_pg_request',views.contacts,name="new_pg_request"),
    path('pg',views.pg,name="pg"),
    path('users',views.user,name="user"),

    
    
]
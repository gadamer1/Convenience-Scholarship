from django.contrib import admin
from django.urls import path
from . import views

app_name= 'userauth'

urlpatterns =[
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('detail/',views.detail_view, name ='detail'),
    path('logout/',views.logout_view,name='logout'),
]
from django.urls import path
from . import views

app_name = 'scholarship'

urlpatterns=[

    #######main##########
    path('main/',views.main , name='main'),
    #######scholarship detail######
    path('scholarship_detail/<slug:scholar_slug>/',views.scholarship_detail,name='detail'),

    path('my_scholar/',views.scholarship_my_scholar,name='my_scholar')
]
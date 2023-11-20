from django.urls import path
from home import views

urlpatterns = [
    path('', views.signin),
    path('pass', views.passwd),
    path('verify', views.verify), 
    path('email', views.email_code),   
    path('phone', views.phone_code),   
    path('2fact', views.two_factor_code), 
]

from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('userlogout/',views.userlogout),
    path('profile/',views.profile),
    path('contect/',views.contect),
    path('about/',views.about),
    path('notes/',views.notes),
    path('otp/',views.otp,name='otp'),
    path('update_profile/',views.update_profile)
]
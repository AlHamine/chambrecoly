from django.urls import path
from . import views

urlpatterns = [
    path('login', views.logIn , name='login'),
    path('logout', views.logOut , name='logout'),
    path('register', views.register, name='register'),
]
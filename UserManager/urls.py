from django.urls import path
from .views import *
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls

urlpatterns=[
    path('login', Login, name='Login'),
    path('logout', Logout, name='Logout'),
    path('list', UserList, name='UserList'),
    path('create', CreateUser, name='CreateUser'),
    


]
from django.urls import path
from .views import *

urlpatterns=[
    path('login', Login, name='Login'),
    path('logout', Logout, name='Logout'),
    path('list', UserList, name='UserList'),
    path('create', CreateUser, name='CreateUser')


]
from django.urls import path
from .views import *

urlpatterns=[
    path('', Dashboard, name='Dashboard'),
    path('message', Message, name='Message')


]
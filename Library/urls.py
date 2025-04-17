from django.urls import path
from .views import *

urlpatterns=[
    path('domain/<int:domain_no>', domain, name='domain')


]
from django.urls import path
from .views import *

urlpatterns=[
    path('quiz/<int:level_no>', Quiz, name='Quiz')


]
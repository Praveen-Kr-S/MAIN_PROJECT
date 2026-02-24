from django.urls import path
from .views import *

urlpatterns = [
    path('',LoginForm,name='login'),
]
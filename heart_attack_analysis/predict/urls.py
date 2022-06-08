from django.urls import path
from .views import *

urlpatterns = [
    path('', main,name='main'),
    path('predict/test01', test01, name='test01'),
    path('predict/calculate', calculate, name='calculate'),
    
]

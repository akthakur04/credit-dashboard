from django.urls import path
from .views import *
urlpatterns = [
    path('',login,name='login'),
    path('home',home,name='home'),
    path('population-chart/', population_chart, name='population-chart'),
    path('newnpachar/', newnpachar, name='newnpachar')

]

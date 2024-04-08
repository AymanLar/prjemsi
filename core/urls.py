from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='index'), 
    path('create/', transaction_create, name='transaction_create'), 
    path('list/', transaction_list, name='transaction_list'), 
    ]

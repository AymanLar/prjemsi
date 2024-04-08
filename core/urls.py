from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='index'), 
    path('transaction/create/', transaction_create, name='transaction_create'), 
    path('transaction/list/', transaction_list, name='transaction_list'), 

    path('budget/create/', budget_create, name='budget_create'),
    path('budget/list/', budget_list, name='budget_list'),
    ]

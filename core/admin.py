from django.contrib import admin
from .models import Transaction, Category
# my little thingies so i can controll them in the admin pnel 
admin.site.register(Transaction)
admin.site.register(Category)
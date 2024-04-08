from django.db import models
from django.contrib.auth.models import User
from emoji import emojize

class Category(models.Model):
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=20, default=':question:', verbose_name='Emoji')
    def __str__(self):
        # return self.name
        return f"{emojize(self.emoji)} {self.name}"

#predefined categories haha with cute little emotescunt
def create_default_categories():
    Category.objects.create(name='Groceries', emoji=':shopping_cart:')
    Category.objects.create(name='Utilities', emoji=':electric_plug:')
    Category.objects.create(name='Entertainment', emoji=':movie_camera:')

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category}: {self.limit}"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description

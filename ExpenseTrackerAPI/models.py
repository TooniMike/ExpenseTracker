from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    
    def __str__(self):
        return self.name
    
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.amount} - {self.category.name}"
    
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.amount} - {self.category.name}"
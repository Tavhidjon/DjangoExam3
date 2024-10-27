from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField( auto_now_add=False)
    category = models.CharField( max_length=50)
    amount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.category

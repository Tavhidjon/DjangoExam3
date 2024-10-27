from django import forms
from .models import *

class Expenseform(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ("user","date","category","amount","description")



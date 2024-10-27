from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from .forms import *

def get_all(request):
    expens = Expense.objects.all()
    return render(request,"get_all.html",context={"expens":expens})


def add(request):
    if request.method == "POST":
        form = Expenseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get")
    else:
        form = Expenseform()
    return render(request,"add.html",context={"form":form})




def edit(request,pk):
    expens = Expense.objects.filter(id=pk).first()
    if expens:
        if request.method == "POST":
            form = Expenseform(request.POST , instance=expens)
            if form.is_valid():
                form.save()
                return redirect("get")
        else:
            form = Expenseform(instance=expens)
        return render(request,"update.html", context={"form":form})
    else:
        return HttpResponse("File not found")
    


def delete(request,pk):
    expens = Expense.objects.filter(id=pk).first()
    if expens:
        if request.method == "POST":
            form = Expenseform(request.POST)
            expens.delete()
            return redirect("get")
        else:
            form = Expenseform()
        return render(request,"delete.html", context={"form":form})
    else:
        return HttpResponse("File not found")
    

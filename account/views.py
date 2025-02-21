from django.shortcuts import render, redirect
from .froms import CustomAccountTypeForm, CustomProjectForm, CustomTransactionForm


def createProject(request):
    if request.method == "POST":
        form = CustomProjectForm(request.POST)
        if form.is_valid():
            form.save() 
            
            return redirect("enterTran")
    
    project_form = CustomProjectForm()

    return render(request, "projectcreate.html", {'project_form':project_form})


def enterTran(request):
    if request.method == "POST":
        form = CustomTransactionForm(request.POST)
        if form.is_valid():
            form.save() 
             
            return redirect("enterTran")
        
    transaction_form = CustomTransactionForm()
    return render(request, 'projectdetails.html', {'transaction_form': transaction_form})


def Taccount(request):
    if request.method == "POST":
        form = CustomAccountTypeForm(request.POST)
        if form.is_valid():
            form.save() 
            
            return redirect("Taccount")

    account_type_form = CustomAccountTypeForm()
    return render(request, 'acctype.html', {'account_type_form': account_type_form})
from django.shortcuts import render, redirect
from .froms import CustomAccountTypeForm, CustomProjectForm, CustomTransactionForm
from django.contrib.auth.decorators import login_required
from .models import Project



@login_required
def viewallproject(request):
    projects = Project.objects.all()
    return render(request, 'viewallproject.html', {"projects" : projects})



@login_required
def createProject(request):
    if request.method == "POST":
        form = CustomProjectForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("enterTran") 
    project_form = CustomProjectForm()
    return render(request, "projectcreate.html", {'project_form':project_form})




@login_required
def enterTran(request):
    if request.method == "POST":
        form = CustomTransactionForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("enterTran")   
    transaction_form = CustomTransactionForm()
    return render(request, 'projectdetails.html', {'transaction_form': transaction_form})



@login_required
def Taccount(request):
    if request.method == "POST":
        form = CustomAccountTypeForm(request.POST)
        if form.is_valid():
            form.save() 
            
            return redirect("Taccount")

    account_type_form = CustomAccountTypeForm()
    return render(request, 'acctype.html', {'account_type_form': account_type_form})


@login_required
def viewstatement(request):
    return render(request, 'viewstatement.html')


@login_required
def viewallproject(request):
    return render(request, 'viewallproject.html')


@login_required
def view_inv(request):
    return render(request, 'view_inv.html')
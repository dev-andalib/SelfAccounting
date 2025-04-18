from django.shortcuts import render, redirect
from .froms import CustomAccountTypeForm, CustomProjectForm, CustomTransactionForm
from django.contrib.auth.decorators import login_required
from .models import Project




@login_required
def viewallproject(request):
    projects = Project.objects.all()  
    return render(request, 'viewallproject.html', {"projects": projects}) 
    


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
def enterTran(request, project_id= None):
    if request.method == "POST":
        form = CustomTransactionForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("enterTran")
    project = Project.objects.get(id = project_id) 
    transaction_form = CustomTransactionForm()
    return render(request, 'projectdetails.html', {'transaction_form': transaction_form, "project" : project})



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









from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product




@login_required
def view_inventory(request):
    data = Product.objects.all()
    return render(request, 'view_inventory.html', {"data": data})


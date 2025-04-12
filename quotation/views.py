from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductEditForm
from django.core.paginator import Paginator



@login_required
def view_inventory(request):
    data = Product.objects.all().order_by('-date_added')  
    paginator = Paginator(data, 10) 

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'view_inventory.html', {'data': data})





@login_required
def edit_product(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()  
            return redirect('view_inventory')  
    else:
        form = ProductEditForm(instance=product)  
    
    return render(request, 'edit_product.html', {'form': form, 'product': product})

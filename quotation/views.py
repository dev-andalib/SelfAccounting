from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductEditForm, ProductForm
from django.core.paginator import Paginator



@login_required
def view_inventory(request):
    data = Product.objects.all().order_by('-date_added')  
    

    usage_location = request.GET.get('usage_location')
    if usage_location:
        data = data.filter(usage_location=usage_location)

    prod_category = request.GET.get('prod_category')
    if prod_category:
        data = data.filter(prod_category=prod_category)


    prod_type = request.GET.get('prod_type')
    if prod_type:
        data = data.filter(prod_type=prod_type)

 
    paginator = Paginator(data, 10) 
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)


    usage_locations = Product.objects.values_list('usage_location', flat=True).distinct()
    categories = Product.objects.values_list('prod_category', flat=True).distinct()
    types = Product.objects.values_list('prod_type', flat=True).distinct()

    return render(request, 'view_inventory.html', {
        'data': data,
        'usage_locations': usage_locations,
        'categories': categories,
        'types': types,

    })

    





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




@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_inventory')  # After adding, go back to inventory list
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})



def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('view_inventory')
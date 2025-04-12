from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
    path('inventory/', views.view_inventory, name = 'view_inventory'),
     path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
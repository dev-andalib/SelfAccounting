from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
    path('inventory/', views.view_inventory, name = 'view_inventory')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
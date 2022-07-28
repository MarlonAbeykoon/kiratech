from django.urls import path

from .views import  InventoryListApiView

app_name = "inventory"

urlpatterns = [
    path('inventory/', InventoryListApiView.as_view())
]
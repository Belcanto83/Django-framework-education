from django.urls import path
from products.views import products_list, products_detail


urlpatterns = [
    path('', products_list),
    path('products_detail/', products_detail)
]

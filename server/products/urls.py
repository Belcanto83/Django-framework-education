from django.urls import path
from products.views import products_list, products_detail

app_name = 'products'

urlpatterns = [
    path('', products_list, name='list'),
    path('<int:idx>/', products_detail, name='detail')
]

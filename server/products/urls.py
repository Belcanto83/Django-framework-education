from django.urls import path
from products.views import products_list, products_detail, product_create, product_update, product_delete


app_name = 'products'

urlpatterns = [
    path('<int:pk>/delete/', product_delete, name='delete_product'),
    path('<int:pk>/update/', product_update, name='update_product'),
    path('create/', product_create, name='create_product'),
    path('', products_list, name='list'),
    path('<int:pk>/', products_detail, name='detail')
]

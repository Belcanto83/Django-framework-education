from django.urls import path
# Импортируем контроллеры из модуля .views
from .views import basket_list, add_to_basket


app_name = 'basket'

urlpatterns = [
    path('', basket_list, name='basket_list'),
    path('add/<int:item>/', add_to_basket, name='add_to_basket')
]

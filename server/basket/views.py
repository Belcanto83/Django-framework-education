from django.shortcuts import render, redirect, get_object_or_404

from .models import OrderedProducts, Orders
from products.models import Product
from accounts.models import AccountUser

from django.urls import reverse_lazy

# Create your views here.


def basket_list(request):
    pass


def add_to_basket(request, item):
    success_url = reverse_lazy('mainapp:main')
    login_url = reverse_lazy('accounts:login')
    product_out_of_stock_url = 'basket/Product out of stock.html'

    if request.user.is_authenticated:
        user = request.user

        try:
            open_order = Orders.objects.get(user_id=user.id, order_is_finished=False)
        except Exception:
            open_order = None

        if open_order is None:
            order = Orders.objects.create(user_id=user.id)
        else:
            order = open_order

        obj = Product.objects.get(id=item)
        if obj.quantity > 0:
            #######################################

            try:
                ordered_product = OrderedProducts.objects.get(order_id=order.id, product_id=obj.id)
                ordered_product.ordered_products_qty += 1
                ordered_product.save()
            except Exception:
                OrderedProducts.objects.create(
                    product_id=obj.id,
                    order_id=order.id,
                )

            #######################################
            obj.quantity -= 1
            obj.save()

            return redirect(success_url)
        else:
            return render(request, product_out_of_stock_url)

    else:
        return redirect(login_url)

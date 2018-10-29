from django.shortcuts import render

import json
from .models import Product

# Create your views here.


def products_list(request):

    # context = {}
    # with open('products/data/products.json', 'r', encoding='UTF-8') as file:
    #     context = json.load(file)
    #
    # return render(request, 'products/Catalogue.html', context)

    query = Product.objects.all()

    return render(request, 'products/Catalogue.html', {'products': query})


def products_detail(request, pk):

    # context = {}
    # with open('products/data/products.json', 'r', encoding='UTF-8') as file:
    #     context = json.load(file)
    #
    # return render(
    #     request,
    #     'products/Product detail.html',
    #     {
    #         'object': context['products'][idx]
    #     }
    # )

    obj = Product.objects.get(id=pk)

    return render(request, 'products/Product detail.html', {'object': obj})

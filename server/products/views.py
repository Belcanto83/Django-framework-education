import json
from django.shortcuts import render

# Create your views here.


def products_list(request):
    context = {}
    with open('products/data/products.json', 'r', encoding='UTF-8') as file:
        context = json.load(file)

    return render(request, 'products/Catalogue.html', context)


def products_detail(request, idx):
    context = {}
    with open('products/data/products.json', 'r', encoding='UTF-8') as file:
        context = json.load(file)

    return render(
        request,
        'products/Product detail.html',
        {
            'object': context['products'][idx]
        }
    )

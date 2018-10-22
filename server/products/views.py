import json
from django.shortcuts import render

# Create your views here.


def products_list(request):
    context = {}
    with open('products/data/products.json', 'r', encoding='UTF-8') as file:
        context = json.load(file)

    return render(request, 'products/Catalogue.html', context)


#TODO Get only one product
def products_detail(request):
    context = {}
    with open('data/products.json', 'r', encoding='UTF-8') as file:
        context = json.load(file)

    return render(request, 'products/Catalogue.html', context)

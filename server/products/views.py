from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.http import Http404, HttpRequest

import json
from .models import Product, Category
from .forms import ProductForm
from django.urls import reverse_lazy

# Create your views here.


def product_delete(request, pk):
    success_url = reverse_lazy('mainapp:main')
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, 'products/delete.html', {'obj': obj})


def product_update(request, pk):
    success_url = reverse_lazy('mainapp:main')

    # try:
    #     obj = Product.objects.get(id=pk)
    # except Exception as err:
    #     raise Http404
    obj = get_object_or_404(Product, pk=pk)

    form = ProductForm(instance=obj)

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(
        request,
        'products/update.html',
        {
            'form': form,
            'obj': obj
        }
    )


def product_create(request):
    form = ProductForm()
    success_url = reverse_lazy('mainapp:main')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def products_list(request):

    # context = {}
    # with open('products/data/products.json', 'r', encoding='UTF-8') as file:
    #     context = json.load(file)
    #
    # return render(request, 'products/Catalogue.html', context)

    # query = Product.objects.all()
    # query = get_list_or_404(Product)[:10]

    selected_category = request.GET.get('category')
    if selected_category is not None:
        selected_category = int(selected_category)

    categories = get_list_or_404(Category)

    if selected_category is not None:
        query = Product.objects.filter(category_id=selected_category)
        page = request.GET.get('page')
        paginator = Paginator(query, 10)
        products = paginator.get_page(page)
    else:
        query = get_list_or_404(Product)
        page = request.GET.get('page')
        paginator = Paginator(query, 10)
        products = paginator.get_page(page)

    if request.method == 'POST':
        requested_category_id = request.POST.get('product_category')
        query = Product.objects.filter(category_id=requested_category_id)
        selected_category = int(requested_category_id)
        page = request.GET.get('page')
        paginator = Paginator(query, 10)
        products = paginator.get_page(page)

        return render(
            request,
            'products/Catalogue.html',
            {
                'products': products,
                'categories': categories,
                'selected_category': selected_category
            }
        )

    return render(
        request,
        'products/Catalogue.html',
        {
            'products': products,
            'categories': categories,
            'selected_category': selected_category
        }
    )


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

    obj = Product.objects.get(pk=pk)

    return render(request, 'products/Product detail.html', {'product': obj})

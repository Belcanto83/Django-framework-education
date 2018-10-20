from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/Contacts.html')


def catalogue(request):
    return render(request, 'mainapp/Catalogue/Catalogue.html')

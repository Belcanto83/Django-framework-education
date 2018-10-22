from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

# Create your views here.


def main(request):
    # template = Template(
    #     'Hello {{ name }} !'
    # )
    template = get_template('mainapp/index.html')
    # context = Context({
    #     'title': 'Привет. Украшения ручной работы Silver Wind'
    # })
    context = {
        'title': 'Украшения ручной работы Silver Wind'
    }
    response_string = template.render(context)
    return HttpResponse(response_string)
    # return render(request, 'mainapp/index.html')


def contacts(request):
    context = {
        'contacts': [
        'Телефон: +7 495 555 55 55',
        'Адрес: г. Москва, Игарский проезд, 12',
        'Почта: gifts@mail.ru'
        ]
    }
    response_string = render_to_string(
        'mainapp/Contacts.html',
        context
    )
    return HttpResponse(response_string)
    # return render(request, 'mainapp/Contacts.html')


def catalogue(request):
    return render(request, 'mainapp/Catalogue/Catalogue.html')

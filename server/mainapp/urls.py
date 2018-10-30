from django.urls import path
from mainapp.views import main, contacts

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),
]

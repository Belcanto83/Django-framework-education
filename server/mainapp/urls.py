from django.urls import path
from mainapp.views import main, contacts


urlpatterns = [
    path('', main),
    path('contacts/', contacts),
]

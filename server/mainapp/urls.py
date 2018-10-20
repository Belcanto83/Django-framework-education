from django.urls import path
from mainapp.views import main, contacts, catalogue


urlpatterns = [
    path('', main),
    path('contacts/', contacts),
    path('catalogue/', catalogue)
]

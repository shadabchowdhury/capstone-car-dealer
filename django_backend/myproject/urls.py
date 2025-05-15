from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Welcome to the Car Dealer App!")

urlpatterns = [
    path('', home),
    # your other paths...
]



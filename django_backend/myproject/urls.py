from django.http import HttpResponse
from django.urls import path

def health_check(request):
    return HttpResponse("OK")

urlpatterns = [
    path('healthz/', health_check),  # add this
    path('', lambda request: HttpResponse("Welcome to Car Dealer!")),  # optional
]




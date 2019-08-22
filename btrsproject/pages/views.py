from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# lets define index function here 

def index(request):
    return HttpResponse("<h1>Hey !! Its time for real estate</h1>")

## Now instead of HttpResponse we gonna render template
def about(request):
    return HttpResponse("<h1>Hey !! Its time for real estate</h1>")
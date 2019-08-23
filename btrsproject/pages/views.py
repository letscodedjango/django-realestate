from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# lets define index function here 


def index(request):
    return HttpResponse("<h1>Hey !! Its time for real estate</h1>")

## Now instead of HttpResponse we gonna render template
def about(request):
    return HttpResponse("<h1>Hey !! Its time for real estate</h1>")


# generally we dont use Httpresponse since the html might be big and hence we always use the concept of html template
def index_template(request):
    return render(request, 'pages/index.html')

## Now instead of HttpResponse we gonna render template
def about_template(request):
    return render(request, 'pages/about.html')
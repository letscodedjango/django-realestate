from django.shortcuts import render
from django.http import request

# Create your views here.

def listings(request):
    return render(request, 'listings/listings.html',{})


def listing(request):
    return render(request, 'listings/listing.html', {})
from django.shortcuts import render

# Create your views here.
def realtors(request):
    return render(request, 'realtors/realtors.html', {})
    # these realtors detail we gonna get from the database so template is not required

def realtor(request):
    return render(request, 'realtors/realtor.html', {})
# these realtors detail we gonna get from the database so template is not required


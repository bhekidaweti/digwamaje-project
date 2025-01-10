from django.shortcuts import render
from .models import Services

# Create your views here.
def home(request):    
    return render(request, 'app/home.html')

def services(request):
    services = Services.objects.all()
    return render(request, 'app/services.html', {'services': services})

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'store/index.html')

def products(request):
    return render(request, 'store/products.html')

def combos(request):
    return render(request, 'store/combos.html')

def contact(request):
    return render(request, 'store/contact.html')

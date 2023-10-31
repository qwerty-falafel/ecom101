from django.shortcuts import render
from oscar.apps.catalogue.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'homepage/home.html', {'products': products})

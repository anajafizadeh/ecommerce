from django.shortcuts import render, HttpResponse
from . import models

def products_list(request):
    products = models.Products.objects.all().order_by('-date')
    
    args = {'products': products}
    return render(request, "products/products_list.html", args)
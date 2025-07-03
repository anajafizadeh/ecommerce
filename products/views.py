from django.shortcuts import render, HttpResponse, redirect
from . import models, forms 
from django.contrib.auth.decorators import login_required

def products_list(request):
    products = models.Products.objects.all().order_by('-date')
    
    args = {'products': products}
    return render(request, "products/products_list.html", args)

def product_details(request, slug):
    product = models.Products.objects.get(slug=slug)
    args = {"product": product}
    return render(request, "products/product_details.html", args)

@login_required(login_url="/accounts/login")
def post(request):
    if request.method == "POST":
        form = forms.PostProduct(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("products:list")
    else:
        form = forms.PostProduct()
    return render(request, "products/post.html", {'form':form})
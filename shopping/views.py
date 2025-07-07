from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Products
from . import models

@login_required(login_url="/accounts/login")
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    
    # Check if item already in cart
    cart_item, created = models.CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('products:list')

def cart_view(request):
    items = models.CartItem.objects.all().order_by('-date_added')
    total = 0
    for item in items:
        total += item.product.price * item.quantity
    return render(request, "shopping/cart.html", {'items':items, 'price': total})

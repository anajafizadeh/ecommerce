from django.urls import path
from . import views

app_name = 'shopping'
urlpatterns = [
    path("add/<int:product_id>", views.add_to_cart, name="add"),
    path("shopping-cart/", views.cart_view, name="shopping-cart"),
]
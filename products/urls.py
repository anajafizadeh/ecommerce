from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path("", views.products_list, name="list"),
    path("post", views.post, name="post"),
    path("<slug>", views.product_details, name="details"),
]

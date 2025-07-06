from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from products.views import products_list


urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include('products.urls')),
    path("accounts/", include('accounts.urls')),
    path("shopping/", include('shopping.urls')),
    path("", products_list),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import ProductViewSet

# Create a router and register our viewset with it.

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
# This will include the URLs for the ProductViewSet, allowing for CRUD operations on products.
# The URLs will be prefixed with 'products/' due to the registration in the router.
# This means you can access the product endpoints at /products/ for listing and creating products,
# and /products/<id>/ for retrieving, updating, and deleting a specific product.

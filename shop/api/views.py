from rest_framework import generics
from shop.models import Category, Product, ProductImages, WishlistItem
from .serializers import CategorySerializer, ProductSerializer, ProductImagesSerializer, WishlistItemSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImagesListCreateView(generics.ListCreateAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer

class WishlistItemListCreateView(generics.ListCreateAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

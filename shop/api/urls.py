from django.urls import path
from .views import CategoryListCreateView, ProductListCreateView, ProductImagesListCreateView, WishlistItemListCreateView

app_name = 'api'
urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product-images/', ProductImagesListCreateView.as_view(), name='product-images-list-create'),
    path('wishlist-items/', WishlistItemListCreateView.as_view(), name='wishlist-item-list-create'),
]
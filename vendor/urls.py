from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.utils.translation import gettext_lazy as _

app_name = 'vendor'


urlpatterns = [
    path('', views.vendors, name="vendors"),
    path('become-vendor/', views.become_vendor, name="become-vendor"),
    path('vendor-admin/', views.vendor_admin, name="vendor-admin"),
    path('edit-vendor/', views.edit_vendor, name="edit-vendor"),

    path('add-product/', views.add_product, name="add-product"),
    path('update_product/<int:id>/<slug:slug>', views.update_product, name="update_product"),
    path('delete_product/<int:id>/<slug:slug>', views.delete_product, name="delete_product"),

    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name="login"),

    path('<int:vendor_id>/', views.vendor, name="vendor"),
    
    #Wishlist
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:id>/<slug:slug>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:id>/<slug:slug>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    
]
    


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Vendor
from shop.models import *
from .forms import ProductForm
from django.views.generic import TemplateView
# Converting Title into Slug
from django.utils.text import slugify

# Create your views here.




def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('shop:product_list')
    else:
        form = UserCreationForm()   

    return render(request, 'vendor/become_vendor.html', {'form': form})


@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()

      

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.name)
            product.save()
    
            return redirect('vendor:vendor-admin')
    else:
        form = ProductForm()
    return render(request, 'vendor/add_product.html', {'form': form})

@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method == 'POST':
        name  = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.save

            return redirect('vendor:vendor-admin')

    return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})


def vendors(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendors.html', {'vendors': vendors})

def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendor/vendor.html', {'vendor': vendor})


@login_required 
def update_product(request, id, slug): 
    product = get_object_or_404(Product, id=id, slug =slug ,vendor=request.user.vendor) 
    if request.method == 'POST': 
        form = ProductForm(request.POST, request.FILES, instance=product) 
        if form.is_valid(): 
            form.save() 
            return redirect('vendor:vendor-admin') 
    else: 
        form = ProductForm(instance=product) 
     
    return render(request, 'vendor/update_product.html', {'form': form}) 



@login_required 
def delete_product(request, id, slug): 
    product = get_object_or_404(Product, id=id, slug =slug ,vendor=request.user.vendor) 
    if request.method == 'POST': 
        product.delete()
        return redirect('vendor:vendor-admin')
    return render(request , 'vendor/delete_product.html')
    
    
    
@login_required
def wishlist(request):
    vendor = request.user.vendor  # Assuming you have authenticated vendors
    wishlist = WishlistItem.objects.filter(vendor=vendor)
    return render(request, 'vendor/wishlist.html', {'wishlist': wishlist})

    
@login_required
def add_to_wishlist(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    vendor = request.user.vendor  # Assuming you have authenticated vendors

    # Check if the product is not already in the wishlist
    if not WishlistItem.objects.filter(vendor=vendor, product=product).exists():
        WishlistItem.objects.create(vendor=vendor, product=product)

    return redirect('vendor:wishlist')  # Redirect to the wishlist page


@login_required
def remove_from_wishlist(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    vendor = request.user.vendor  # Assuming you have authenticated vendors

    # Check if the product is in the wishlist
    if WishlistItem.objects.filter(vendor=vendor, product=product).exists():
        wishlist_item = WishlistItem.objects.get(vendor=vendor, product=product)
        wishlist_item.delete()

    return redirect('vendor:wishlist')  # Redirect to the wishlist page
    
    
    

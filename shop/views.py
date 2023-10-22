import random
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.db.models import Q


# Create your views here.

def product_list(request , category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available =True)
    new_products = Product.objects.filter(available=True).order_by('-created')[:10]
    
    # Get 8 products from each category
    products2 = {}
    categories2 = Category.objects.prefetch_related('products').all()
    for category in categories2:
        products2[category.name] = list(category.products.all()[:6])
        
    

    
    return render(request, 'product_list.html', {'category': category,
                                                'categories': categories,
                                                'products': products,
                                                'new_products':new_products,
                                                'products2': products2,})
     

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    # Get similar products
    similar_products = list(product.category.products.exclude(id=product.id))
    
    # If more than 4 similar products, then get 4 random products 
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    
    return render(request, 'product_detail.html', {'product': product,
                                                   'similar_products': similar_products,})

def search(request):
    query = request.GET.get('query','') # second is default parameter which is empty
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'search.html' , {'products':products,
                                                    'query':query})
    
    
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request,'category.html', {'category': category})




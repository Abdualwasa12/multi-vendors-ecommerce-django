from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from vendor.models import Vendor
from django.utils.translation import gettext_lazy as _

# Create your models here.




#----Model class----
class Category(models.Model):
    name = models.CharField( max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category', blank=True, default="default.png")
    class Meta:
        # ordering = ['name']
        verbose_name ='category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:products_by_category',
                       args=[self.slug])


    
    
class Product(models.Model):

    name = models.CharField(_('Name'), max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(_('Description'), blank=True)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    phone = models.PositiveIntegerField(_('Phone'), blank=True)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, blank=True)
    available = models.BooleanField(_('Available'), default=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    thumbnail = models.ImageField(_('Thumbnail'), upload_to='product_thumb/', blank=True)

   


    class Meta:
        ordering = ('-created',)
        # index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class ProductImages(models.Model):
   product_image = models.ForeignKey(Product, on_delete=models.CASCADE)
   image = models.ImageField(_('Image'), upload_to='products/', blank=True)

class WishlistItem(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    added_at = models.DateTimeField(_('Added at'), auto_now_add=True)
    class Meta:
        unique_together = ('vendor', 'product')



        
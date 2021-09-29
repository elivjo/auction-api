from django.contrib import admin

# Register your models here.
from .models import Product, UserProfile, Bid

admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Bid)
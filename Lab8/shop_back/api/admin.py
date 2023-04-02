from django.contrib import admin
from api.models import Category
from api.models import Product

admin.site.register(Product)
admin.site.register(Category)
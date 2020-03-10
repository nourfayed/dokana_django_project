from django.contrib import admin
from .models import Category, Products, SubCategory

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(SubCategory)
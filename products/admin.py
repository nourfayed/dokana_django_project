from django.contrib import admin
from .models import Category, Products, SubCategory, Reviews

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(SubCategory)
admin.site.register(Reviews)

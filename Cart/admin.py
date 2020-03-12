from django.contrib import admin

# Register your models here.
from .models import Cart, Products, User, History

admin.site.register(Cart)
admin.site.register(History)
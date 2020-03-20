from django.contrib import admin

# Register your models here.
from .models import Cart, Products, User, History,Favourite

admin.site.register(Cart)
admin.site.register(History)
admin.site.register(Favourite)
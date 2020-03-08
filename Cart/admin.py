from django.contrib import admin

# Register your models here.
from Cart.models import Cart, History

admin.site.register(Cart)
admin.site.register(History)
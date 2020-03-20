from django.contrib import admin
from django.urls import path, include

from Cart import views

urlpatterns = [
    path('', views.AddToCart, name="cart"),
    path('show/', views.showCart, name="Show cart"),
    path('checkout/', views.checkout, name="Show cart"),

    path('', views.AddToFavourite, name="favourite"),
    path('showfav/', views.showFavourite, name="Show cart"),
    path('checkFavoute/', views.checkFavoute, name="Show cart"),
    # path('',views.GetCart,name = "get")
]

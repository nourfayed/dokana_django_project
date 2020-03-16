from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('productDetails/', views.showDetails),
    path('search/', views.search, name="search")
]
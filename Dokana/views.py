from django.forms import forms
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from Cart.models import Cart
from products.models import Category


class HomePageView(ListView):
    model = Category
    template_name = 'ProductsSideBySide.html'


class CartPageView(ListView):
    model = Cart
    template_name = 'Cart.html'


class TestPageView(ListView):
    model = Cart
    template_name = 'te.html'


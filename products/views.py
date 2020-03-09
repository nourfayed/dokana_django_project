from django.shortcuts import render
from .models import Category, Products


#Create your views here.
def index(request):
  
   latest_products= Products.objects.get(pk=1)
   print("w eh kaman")
   print(latest_products)
   Data= {'latest_products':latest_products}
   return render(request, 'products/index.html',Data)

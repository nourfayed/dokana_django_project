from django.shortcuts import render
from .models import Category, Products


#Create your views here.
def index(request):
   products=Products()
   latest_products= products.getProductsByCategory(2)
   print("w eh kaman")
   print(latest_products)
   Data= {'latest_products': latest_products}
   return render(request , 'products/index.html', Data)

from django.shortcuts import render
from .models import Category, Products


def index(request):
    products = Products()
    latest_products = products.getAllProducts()
    print("w eh kaman")
    print(latest_products)
    data = {'latest_products': latest_products}
    return render(request, 'products/index.html', data)


def showDetails(request):
    currentProductId = request.POST.get('productID', '')

    print("current product id----------------------")
    print(currentProductId)
    product = Products.objects.get(productID=currentProductId)
    print("mn gowa sho details")
    print(product.productID)
    data = {'product': product}
    return render(request, "products/productDetails.html", data)

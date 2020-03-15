from django.shortcuts import render, redirect
from .models import Category, Products
from .forms import ReviewForm
from User.models import User


def index(request):
    products = Products()
    latest_products = products.getAllProducts()
    data = {'latest_products': latest_products}
    return render(request, 'products/index.html', data)


def showDetails(request):
    currentProductId = request.POST.get('productID', '')
    print("Current product id from show details................................")
    print(currentProductId)
    product = Products.objects.get(productID=currentProductId)

    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.productID = product
        user = User()
        user.userId=1
        user.userName = "7amada"
        user.email = "fgklhkk@gmail.com"
        user.password = "12435465rydf"
        user.phone =1234546
        user.save()
        review.userID = user
        review.save()
    data = {'product': product, 'form': form}
    return render(request, "products/productDetails.html", data)



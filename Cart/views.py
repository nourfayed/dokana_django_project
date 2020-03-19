from django.shortcuts import render

from Cart.models import Cart, Products, User


def AddToCart(request):
    print(request)
    text1 = request.POST.get('text1')
    print(text1)
    text2 = request.POST.get('text2')
    print(text2)
    cart = Cart(productID=Products.objects.get(productID=text1), userID=User.objects.get(userId=text2))
    cart.save()
    test = tuple(Cart.objects.filter(userID=text2))
    return render(request, 'Cart.html' ,{'Cart':test})

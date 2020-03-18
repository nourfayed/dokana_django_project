from django.shortcuts import render

from Cart.models import Cart, Products, User


def AddToCart(request):
    print(request)
    product_Id = request.POST.get('text1')
    print(product_Id)
    user_id = request.POST.get('text2')
    print(user_id)
    if not _chk_cart(userId=user_id, productId=product_Id):
        cart = Cart(productID=Products.objects.get(productID=product_Id), userID=User.objects.get(userId=user_id))
        cart.save()
    test = tuple(Cart.objects.filter(userID=user_id))
    return render(request, 'Cart.html', {'Cart': test})


def showCart(request):
    user_id = request.session['id']
    test = tuple(Cart.objects.filter(userID=user_id))
    return render(request, 'Cart.html', {'Cart': test})


def _chk_cart(userId, productId):
    userCarts = Cart.objects.filter(userID=userId)
    if userCarts:
        if Cart.objects.filter(userID=userId, productID=productId):
            return True
        else:
            return False
    return False

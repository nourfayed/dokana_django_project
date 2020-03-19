from django.shortcuts import render, redirect
from django.utils import timezone

from Cart.models import Cart, Products, User, History,Favourite


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


def checkout(request):
    user_carts = tuple(Cart.objects.filter(userID=request.session.get('id')))
    print(request.POST)
    if 'check' in request.POST:
        for cart in user_carts:
            count = request.POST.get('count-' + str(cart.productID.productID))
            pay = request.POST.get('options')
            History(userID=cart.userID, productID=cart.productID, count=count, date=timezone.now(),
                    paymentMethod=pay).save()
            cart.delete()
            return redirect("/profile/" + str(request.session.get('id')) + "/history")

    else:
        for cart in user_carts:
            if 'del-' + str(cart.productID.productID) in request.POST:
                cart.delete()
        return redirect("/cart/show/")

# view Favourite fuctions 

def _chk_fav(userId, productId):
    userFav = Favourite.objects.filter(userID=userId)
    if userFav:
        if Favourite.objects.filter(userID=userId, productID=productId):
            return True
        else:
            return False
    return False


def checkFavoute(request):
    user_Fav = tuple(Favourite.objects.filter(userID=request.session.get('id')))
    
    if 'check' in request.POST:
        for fav in user_Fav:
             
            fav.delete()
            return redirect("/profile/" + str(request.session.get('id')))

    else:
        for fav in user_Fav:
            if 'del-' + str(fav.productID.productID) in request.POST:
                fav.delete()
        return redirect("/fav/showfav/")

def AddToFavourite(request):
    product_Id = request.POST.get('text1')
    user_id = request.POST.get('text2')
     
    if not _chk_fav(userId=user_id, productId=product_Id):
        fav = Favourite(productID=Products.objects.get(productID=product_Id), userID=User.objects.get(userId=user_id))
        fav.save()
    test = tuple(Favourite.objects.filter(userID=user_id))
    return render(request, 'favourite.html', {'favourite': test})

def showFavourite(request):
    user_id = request.session['id']
    test = tuple(Favourite.objects.filter(userID=user_id))
    return render(request, 'favourite.html', {'favourite': test})
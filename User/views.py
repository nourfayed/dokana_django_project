from django.shortcuts import render

# Create your views here.
from Cart.models import History
from User.forms import ChangePasswordForm
from User.models import User, Address

import logging

from products.models import Products


def profile(request, pk):
    user_profile = User.objects.get(userId=pk)
    addresses = Address.objects.filter(userID=pk)

    return render(request, 'user/profile.html',
                  {'profile': user_profile, 'address1': addresses[0].address, 'address2': addresses[1].address})


def history(request, pk):
    user_profile = User.objects.get(userId=pk)
    user_history = History.objects.filter(userID=pk)
    products = []
    for h in user_history:
        p = Products.objects.get(productID=h.productID.productID)
        product = {
            'data': p,
            'pay': h.paymentMethod
        }
        products.append(product)

    return render(request, 'user/history.html', {'user': user_profile.userName, 'history': products})


def changePass(request, pk):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        # change password
        if form.is_valid():
            user = User.objects.get(userId=pk)
            if user.password == request.POST.get('old_password', ''):
                user.password = request.POST.get('new_password', '')
                user.save()
                return render(request, 'user/pass_ok.html')
    else:
        form = ChangePasswordForm()

    return render(request, 'user/ch_password.html', {'form': form})

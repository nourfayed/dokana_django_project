from django.shortcuts import render

# Create your views here.
from User.models import User, Address


def profile(request, pk):
    user_profile = User.objects.get(userId=pk)
    addresses = Address.objects.filter(userID=pk)

    return render(request, 'user/profile.html', {'profile': user_profile, 'address1': addresses[0].address, 'address2': addresses[1].address})

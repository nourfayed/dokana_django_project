from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate
# Create your views here.
from Cart.models import History
from Dokana.models import Product
from User.forms import ChangePasswordForm
from User.models import User, Address
from .forms import RegisterForm
import logging

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'user/register.html'


    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        print("sssss"+form.data.get('username'))

        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(userName=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.data.get('username'),
                    form.data.get('email'),
                    form.data.get('password'),
                    form.data.get('Image'),
                    form.data.get('phone_number')
                )
                # user.first_name = form.cleaned_data['first_name']
                # user.last_name = form.cleaned_data['last_name']
                # user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                 

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()
    return render(request, template, {'form': form})


# login authentication

def user_login(request):
    if request.method == 'POST':
         
        # username = request.POST['username']
        # password = request.POST['password'] 
        username = request.POST.get('userName','')
        password = request.POST.get('password','')
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        # user_name=User.objects.get(userName=username)
        # user_password=User.objects.get(password=password)
        # if (user_name==)
         
        if user:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'user/profile.html')
        else:
            #   throw an error to the screen.
            return render(request, 'user/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'user/login.html')


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
        p = Product.objects.get(productID=h.productID.productID)
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

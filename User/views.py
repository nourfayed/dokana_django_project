from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
# Create your views here.
from Cart.models import History
from User.forms import ChangePasswordForm, ImageForm
from User.models import User, Address
from .forms import RegisterForm, ImageUploadForm
import logging


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'user/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        photo_upload_form = ImageUploadForm(request.POST, request.FILES)
        print("sssss" + form.data.get('username'))

        #     context = {
        #     "form": form,
        #     "photo_upload_form": photo_upload_form
        # }
        # check whether it's valid:
        if form:
            if User.objects.filter(userName=form.data.get('username')):
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.data.get('email')):
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.data.get('password') != form.data.get('password_repeat'):
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })

            else:
                # Create the user:
                user = User.create_user(
                    form.data.get('username'),
                    form.data.get('email'),
                    form.data.get('password'),
                    form.data.get('Image'),
                    form.data.get('phone_number')
                )
                # user.first_name = form.cleaned_data['first_name']
                # user.last_name = form.cleaned_data['last_name']
                # user.phone_number = form.cleaned_data['phone_number']
                # user.save()



    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()
    return render(request, template, {'form': form})


# login authentication
user_status=False # flag check if the user logged in ?
def user_login(request):
    if request.method == 'POST':

        # username = request.POST['userName']
        # password = request.POST['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check username and password combination if correct
        try:
            user=User.objects.get(userName=username)
        except:
            return render(request, 'user/login.html', {'error_message': 'Incorrect username and / or password.'})
        
        if user is not None:
            # Save session as cookie to login the user
             
            if user.password == password:
                # login(request, user)
            # Success, now let's login the user.
                user_status=True
                request.session['logged'] = True
                request.session['id'] = user.userId
                return redirect('/profile/'+user.userId.__str__())
            else:
            #   throw an error to the screen.
                return render(request, 'user/login.html', {'error_message': 'Incorrect username and / or password.'})
        else:
            #   throw an error to the screen.
            return render(request, 'user/login.html', {'error_message': 'Incorrect username and / or password.'})
            
    else:
        return render(request, 'user/login.html')


from products.models import Products


def profile(request, pk):
    user_profile = User.objects.get(userId=pk)
    addresses = Address.objects.filter(userID=pk)
    imageForm = ImageForm()

    return render(request, 'user/profile.html',
                  {'profile': user_profile, 'img_form': ImageForm, 'address1': addresses[0].address, 'address2': addresses[1].address})


def history(request, pk):
    user_profile = User.objects.get(userId=pk)
    user_history = History.objects.filter(userID=pk)
    history = []
    for h in user_history:
        p = Products.objects.get(productID=h.productID.productID)
        product = {
            'product_data': p,
            'data': h
        }
        history.append(product)

    return render(request, 'user/history.html', {'user': user_profile.userName, 'history': history})


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
                return render(request, 'user/ch_password.html', {'form': form, 'e': "Old Password Incorrect"})

    else:
        form = ChangePasswordForm()

    return render(request, 'user/ch_password.html', {'form': form})

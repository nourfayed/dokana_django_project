"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from Django_project import settings
from User import views
from products import views as products_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('products/', include('products.urls')),
                  path('profile/', include('User.urls')),
                  path('register/', views.user_register, name='user_register'),
                  path('logout/', views.logout, name='logout'),
                  path('deactivate/',views.delete_profile,name='deactivate'),
                  #    path('',views.signup_view,name="signup")
                  path('Login/', views.user_login, name="Login"),
                  path('search/', products_views.search, name="search"),
                  # path('', include('products.urls')),
                  path('', include('Dokana.urls')),
                  path('cart/', include('Cart.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

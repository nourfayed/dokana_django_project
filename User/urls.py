from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.profile, name='profile'),
    path('<int:pk>/history/',views.history, name='History'),
    path('<int:pk>/changePassword/', views.changePass, name='Change Password'),
    path('register/', views.user_register, name='user_register'),
#    path('',views.signup_view,name="signup")
    path('Login/',views.user_login,name="Login")
]
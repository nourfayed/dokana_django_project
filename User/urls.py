from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.profile, name='profile'),
    path('<int:pk>/history/',views.history, name='History'),
    path('<int:pk>/changePassword/', views.changePass, name='Change Password'),
    path('<int:pk>/logout/', views.logout, name='logout'),
    path('<int:pk>/deactivate/', views.delete_profile, name='logout'),


]
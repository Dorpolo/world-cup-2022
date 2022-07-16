from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('league-members/', views.profiles, name='profiles'),
    path('profile-builder/', views.ProfileBuilder().create, name='profile-builder'),
]

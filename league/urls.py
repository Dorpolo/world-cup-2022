from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.LeagueBuilder().create, name='create-league'),
    path('update/<str:pk>', views.LeagueBuilder().update, name='update-league'),
    path('join/', views.LeagueMembership().create, name='league-membership'),
    path('fan-zone/', views.my_leagues, name='league-zone'),
]

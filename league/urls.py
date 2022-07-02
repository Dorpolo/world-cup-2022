from django.urls import path

from . import views

urlpatterns = [
    path('new-league/', views.LeagueBuilder().create, name='create-league'),
    path('league/<str:pk>', views.LeagueBuilder().update, name='update-league'),
    path('join-a-league/', views.LeagueMembership().create, name='league-membership'),
    path('league-zone/', views.my_leagues, name='league-zone'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.game_results, name='predictions'),
    path('game_result/<str:pk>', views.game_result, name='single_prediction')
]
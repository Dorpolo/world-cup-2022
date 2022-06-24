from django.urls import path

from . import views

urlpatterns = [
    path('leagues/', views.league, name='league'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.predictions, name='predictions'),
    path('single_match_prediction/<str:pk>', views.single_prediction, name='single_prediction')
]

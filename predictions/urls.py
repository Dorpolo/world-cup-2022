from django.urls import path

from . import views

urlpatterns = [
    path('grouo-stage-prediction', views.group_stage_prediction, name='group-stage-prediction'),
    path('single_match_prediction/<str:pk>', views.single_match_prediction, name='single_match_prediction')
]

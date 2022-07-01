from django.urls import path

from common.api.results_api import StageType
from . import views

urlpatterns = [
    path('', views.CRUDPrediction(stage_type=StageType.GROUP).create, name='group-stage-prediction'),
    path('prediction/group-stage', views.CRUDPrediction(stage_type=StageType.GROUP).create, name='group-stage-prediction'),
    path('prediction/final/', views.CRUDPrediction(stage_type=StageType.KNOCKOUT_2).create, name='final-prediction'),
    path('prediction/final/<str:pk>/', views.CRUDPrediction(stage_type=StageType.KNOCKOUT_2).update, name='update-final-prediction'),
]

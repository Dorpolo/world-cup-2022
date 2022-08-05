from django.urls import path

from common.api.results_api import StageType
from . import views

urlpatterns = [
    path('group-stage/', views.CreateView.as_view(), name='group-stage-prediction'),
    path('final/<str:pk>/', views.CRUDPrediction(stage_type=StageType.KNOCKOUT_2).update, name='update-final-prediction'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]

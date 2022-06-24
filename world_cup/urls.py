from django.contrib import admin
from django.urls import path, include

from predictions.views import single_match_prediction, predictions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predictions.urls')),
    path('', include('league.urls')),
]

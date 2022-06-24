from django.contrib import admin
from django.urls import path, include

from game_results.views import game_result, game_results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game_results.urls')),
]


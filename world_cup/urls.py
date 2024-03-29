from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import users.views
import world_cup.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', world_cup.views.view_nav_bar, name='navbar'),
    path('predict/', include('predictions.urls')),
    path('leagues/', include('league.urls')),
    path('users/', include('users.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




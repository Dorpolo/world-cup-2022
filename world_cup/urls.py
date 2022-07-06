from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users.views.profiles, name='profiles'),
    path('predict/', include('predictions.urls')),
    path('leagues/', include('league.urls')),
    path('users/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from applications import views as app_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Browser-reload endpoint (only in DEBUG)
    # so reverse("django_browser_reload:events") works
    *(
        [path("__reload__/", include("django_browser_reload.urls"))]
        if settings.DEBUG
        else []
    ),

    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),

    # Application routes
    path('jobs/', include('applications.urls')),
    path('signup/', include('applications.urls')),
    path('logout/', include('applications.urls')),

    # Landing page
    path('', app_views.home, name='home'),
]
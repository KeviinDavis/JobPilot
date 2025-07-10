"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include
from applications import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),

    # Application routes
    path('jobs/', include('applications.urls')),
    path('signup/', include('applications.urls')),
    path('logout/', include('applications.urls')),

    # Landing page
    path('', app_views.home, name='home'),
]
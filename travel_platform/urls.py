"""travel_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('places/', include('places.urls')),
    path('packages/', include('packages.urls')),
    path('bookings/', include('bookings.urls')),
    path('feedback/', include('feedback.urls')),
    path('events/', include('events.urls')),
    path('itinerary/', include('itinerary.urls')),
    path('payments/', include('payments.urls')),
    path('admin-dashboard/', include('admin_dashboard.urls')),
    path('i18n/', include('django.conf.urls.i18n')),  # Language switching
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
URL configuration for CyberXpert project.

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
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from two_factor.urls import urlpatterns as tf_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('UserManager.urls', 'UserManager'), namespace='UserManager')),
    path('', include(('Dashboard.urls', 'Dashboard'), namespace='Dashboard')),
    path('lesson/', include(('Lesson.urls', 'Lesson'), namespace='Lesson')),
    path('library/', include(('Library.urls', 'Library'), namespace='Library')),
    path('mfa/', include(tf_urls, namespace='two_factor')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
URL configuration for divar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import include
from authentication.views import CreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('users/', TokenObtainPairView.as_view(), name='user_create'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]))
]+debug_toolbar_urls()

"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .api.docktor import get_available_times, docktors
from .api.users import register, login, log_out

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/available_times', get_available_times, name='available_times'),
    path('api/register', register),
    path('api/login', login),
    path('api/logout', log_out),
    path("home", docktors)
]

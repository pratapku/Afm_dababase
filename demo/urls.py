"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.authtoken import views
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
# from app import views
from app import views as myapp_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.obtain_auth_token),
    path('',include('app.urls')),
    path('addyourdevice/', myapp_view.deviceList),
    path('getyourdevice/', myapp_view.devicegetList),
    path('getallyourdevice/', myapp_view.devicegetallList),
    path('getpostdevicePinStatus/', myapp_view.devicePinStatus),
    path('getpostdevicePinName/', myapp_view.devicePinName),

    

    path('getuid/', myapp_view.useridList),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

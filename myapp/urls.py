from django.urls import path,include
from django.conf import settings
from . import views
from . views import *

from .views import  UserDetailAPI,RegisterUserAPIView

from .import views

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('' , views.index,),
    path('api/register/',RegisterUserAPIView.as_view()),
    


]
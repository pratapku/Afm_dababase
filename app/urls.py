"""Afm URL Configuration

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
from django.urls import path
from app import views
from app import views as app_view
from .import views
from .views import UserDetailAPI,RegisterUserAPIView

urlpatterns = [
   
    path('',views.index),
    path('register/',RegisterUserAPIView.as_view()),
    path('addyourplace/',app_view.placeList),
    path('getallplaces/', app_view.placegetList),
                   ###
    path('getallplacesbyonlyplaceidp_id/', app_view.placegetallList),
    path('addyourfloor/',app_view.fieldList),
    path('getallfield/', app_view.fieldgetList),
    ####
    path('getallfloorsbyonlyplaceidp_id/', app_view.fieldgetallList),
    ##
    path('pin/',views.pinname.as_view()),
    path('pinsupdate/<int:pk>/',views.pinRetrieveUpdateDestroy.as_view()),
    #Subuseraccess
    path('subuseraccess/',views.Subuseraccess.as_view()),
    path('subuseraccessupdate/<int:pk>/',views.SubuseraccessRetrieveUpdateDestroy.as_view()),
    #
    path('place/',views.Place.as_view()),
    path('placeupdate/<int:pk>/',views.PlaceRetrieveUpdateDestroy.as_view()),
    #
    path('subuserplace/',views.Subuserplace.as_view()),
    path('subuserplaceupdate/<int:pk>/',views.SubuserplaceRetrieveUpdateDestroy.as_view()),
        ######
    path('giveaccesstotempuser/', app_view.tempU),
    path('getalldatayouaddedtempuser/', app_view.tempulist),
]
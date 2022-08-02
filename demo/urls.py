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
from myapp import views as myapp_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', views.obtain_auth_token),
    path('',include('myapp.urls')),

    path('getthedataofuser/',myapp_view.userdataList),
    path('addyourplace/',myapp_view.placeList),
    path('addyourfield/',myapp_view.fieldList),

    path('addyourdevice/', myapp_view.deviceList),
    path('getallplaces/', myapp_view.placegetList),
    path('getallfields/', myapp_view.fieldgetList),
    path('getallplacesbyonlyplaceidp_id/', myapp_view.placegetallList),
    path('getallfieldsbyonlyplaceidp_id/', myapp_view.fieldgetallList),
    path('getpostdeviceStatus/', myapp_view.devicePinStatus),
    path('webhookapi/', myapp_view.webhook),
    # path('getpostPinName/',myapp_view.devicePinNames),
    path('subuseraccess/', myapp_view.subuaccess),
    path('subuserpalceaccess/', myapp_view.subuplace),
    ################       user related path         ##########################
    # path('login/',myapp_view.Login,name='login'),
    # path('logout/',auth.LogoutView.as_view(template_name='user/index.html'),name='logout'),
    # path('register/',myapp_view.register,name='register'),

    # path('addyourflat/',myapp_view.flatList),
    # path('addroom/', myapp_view.roomList),
    # path('schedulingpinsalltheway/',myapp_view.pinscheduling),
    # path('scheduledatagetbyid/', myapp_view.pinschedulingdevice),
    

    # path('getallflats/', myapp_view.flatgetList),
    # path('getallrooms/', myapp_view.roomgetList),
    
    # path('getallflatbyonlyflooridf_id/', myapp_view.flatgetallList),
    # path('getallroomsbyonlyflooridf_id/', myapp_view.roomgetallList),
    path('getalldevicesbyonlyfieldf_id/', myapp_view.devicegetallList),
    
    # path('getpostemergencynumber/', myapp_view.emerNumber),
    # path('tensensorsdata/', myapp_view.sensorsList),
    # path('ssidpassword/', myapp_view.ssidList),
    # path('editpinnames/', myapp_view.devicePinNames),
    # path('addprofileimage/', myapp_view.profoto),
    # path('addipaddress/', myapp_view.ipaddressList),
    # path('subuserfindall/', myapp_view.subuserfind),
    # path('subfindsubdata/', myapp_view.subuserfindsubuser),


###############  Getting Names    ####################
    # path('getyoufloorname/', myapp_view.floornamelist),
    # path('getyouflatname/', myapp_view.flatnamelist),
    # path('getyouroomname/', myapp_view.roomnamelist),


########## for main user to get the list of subuser  ##############
    path('getyouplacename/', myapp_view.placenamelist),
    path('getuid/', myapp_view.useridList),
    path('getalldatayouadded/', myapp_view.subuplaceget),
    path('getalldatayouaddedtempuser/', myapp_view.tempulist),

########## for main user to get the list of temporary user  ##############

######### tamporary user otp login #######################

    # path('giveaccesstotempuser/', myapp_view.tempU),
    # path('loginotpsend/', myapp_view.tempu),
    # path('tempuserloginwithotp/', myapp_view.tempulogin),
    # path('tempuserautodelete/', myapp_view.tempuserautodelete),

    ###### Bill pridiction #############3

    # path('energyconsume/', myapp_view.enerzyList),
    # path('pertenminuteenergy/',myapp_view.pertenminute),
    # path('perhourenergy/',myapp_view.perhour),
    # path('perdaysenergy/',myapp_view.perday),
    # path('peryearenergy/',myapp_view.peryear),






    # path('testkrlo/', myapp_view.my_django_view)

    # path('testimages123/', myapp_view.testimages123),


    # path('user/',views.employeesList.as_view()),
    # path('firmwareupdate/', myapp_view.firmwareupdate),
    # path('firmwarecheck/', myapp_view.firmwarecheck),
    

    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

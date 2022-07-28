
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(field)
class CusAdmin(admin.ModelAdmin):
    list_display= ('id',)
admin.site.register(allDevices)

admin.site.register(device)

admin.site.register(Device_status)

admin.site.register(Pin_name)
admin.site.register(subuseraccess)
admin.site.register(place)
class PlaceAdmin(admin.ModelAdmin):
    list_display= ('user','p_id')

admin.site.register(subuserplace)
admin.site.register(tempuser)


 


   
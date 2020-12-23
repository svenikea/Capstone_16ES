from django.contrib import admin
from .models import Parking, Parkinglotlist, Stafflist, History, \
        Cameralist
# Register your models here.
admin.site.register(Parking)
admin.site.register(Parkinglotlist)
admin.site.register(Stafflist)
admin.site.register(History)
admin.site.register(Cameralist)

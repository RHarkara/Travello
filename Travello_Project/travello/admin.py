from django.contrib import admin

# Register your models here.

from . models import Destination, WarangalDetails

admin.site.register(Destination),
admin.site.register(WarangalDetails)
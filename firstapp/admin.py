from django.contrib import admin

# Register your models here.
from .models import places  #for admin panel
admin.site.register(places)

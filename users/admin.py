from django.contrib import admin
from .models import Profile, Family


admin.site.register(Profile)                #to let admin see this model
admin.site.register(Family)                 #to let admin see this model


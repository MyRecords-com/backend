from django.contrib import admin

# Register your models here.
from .models import Profile, Record

#Register Your Models Here
admin.site.register(Profile)
admin.site.register(Record)
from django.contrib import admin

# Register your models here.
from .models import Profile, Record, Collection, Comment

#Register Your Models Here
admin.site.register(Profile)
admin.site.register(Record)
admin.site.register(Collection)
admin.site.register(Comment)
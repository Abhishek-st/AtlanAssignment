from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Question)
admin.site.register(Type)
admin.site.register(UserResponse)
admin.site.register(Form)
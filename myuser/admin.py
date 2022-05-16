from csv import list_dialects
from django.contrib import admin
from .models import Myuser, Center, Test

# Register your models here.
class MyuserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password','email','position','department']


class CenterAdmin(admin.ModelAdmin):
    list_display = ['middleTime', 'username', 'position', 'department']

class TestAdmin(admin.ModelAdmin):
    list_display = ['dateTimeOfAM', 'dateTimeOfPM', 'username', 'position', 'department']
    
admin.site.register(Myuser, MyuserAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(Test, TestAdmin)
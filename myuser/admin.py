from csv import list_dialects
from django.contrib import admin
from .models import Myuser, Start, End, Center, Test

# Register your models here.
class MyuserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password','email','position','department']

class StartAdmin(admin.ModelAdmin):
    list_display = ['dateTimeOfAM', 'username', 'position', 'department']

class EndAdmin(admin.ModelAdmin):
    list_display = ['dateTimeOfPM', 'username', 'position', 'department']

class CenterAdmin(admin.ModelAdmin):
    list_display = ['middleTime', 'username', 'position', 'department']

class TestAdmin(admin.ModelAdmin):
    list_display = ['dateTimeOfAM', 'dateTimeOfPM', 'username', 'position', 'department']
    
admin.site.register(Myuser, MyuserAdmin)
admin.site.register(Start, StartAdmin)
admin.site.register(End, EndAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(Test, TestAdmin)
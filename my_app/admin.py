from django.contrib import admin

# Register your models here.
from .models import Database
@admin.register(Database)
class DataAdmin(admin.ModelAdmin):
    list_display=('Name','DateOfBirth','PhoneNumber','EmailID')
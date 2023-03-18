from django.contrib import admin
from .models import House_Location

# Register your models here.
@admin.register(House_Location)
class House_LocationAdmin(admin.ModelAdmin):
    list_display = ['location', 'slug']
    prepopulated_fields = {'slug': ('location',)}

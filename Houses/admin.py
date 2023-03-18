from django.contrib import admin
from .models import House_Location, House_Details

# Register your models here.
@admin.register(House_Location)
class House_LocationAdmin(admin.ModelAdmin):
    list_display = ['location', 'slug']
    prepopulated_fields = {'slug': ('location',)}

@admin.register(House_Details)
class House_DetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'monthly_rent', 'owners_contact', 'available', 'updated']

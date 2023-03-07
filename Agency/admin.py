from django.contrib import admin
from .models import House_Location, House_Details

# Register your models here.
@admin.register(House_Location)
class House_LocationAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'slug']
    prepopulated_fields = {'slug': ('location_name',)}

@admin.register(House_Details)
class House_DetailsAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug', 'rent_amount', 'available', 'posted', 'updated']
    list_filter = ['available', 'posted', 'updated']
    list_editable = ['rent_amount', 'available']
    prepopulated_fields = {'slug': ('category_name',)}

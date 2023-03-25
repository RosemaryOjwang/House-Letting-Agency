from django.contrib import admin
from .models import House_Location, House_Details, MultipleImage

# Register your models here.
@admin.register(House_Location)
class House_LocationAdmin(admin.ModelAdmin):
    list_display = ['locationName', 'slug']
    prepopulated_fields = {'slug': ('locationName',)}

@admin.register(House_Details)
class House_DetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'monthly_rent', 'owners_contact', 'available', 'updated']
    list_filter = ['available', 'posted', 'updated']
    list_editable = ['monthly_rent', 'available']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(MultipleImage)
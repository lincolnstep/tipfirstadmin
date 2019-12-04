from django.contrib import admin

# Register your models here.
from .models import HotelDetail
from import_export.admin import ImportExportModelAdmin

class HotelDetailAdmin(ImportExportModelAdmin):
    list_display = ('id','location', 'hoteltype', 'category', 'hotelname', 'mealplan', 'pax', 'peak','mid','off')
    list_display_links = ('location','hoteltype')
    list_filter = ('location','hoteltype','category','mealplan', 'hotelname')
    list_editable = ('peak', 'mid','off',)
    search_fields = ('location', 'hotelname', 'category')
    list_per_page = 25

admin.site.register(HotelDetail,HotelDetailAdmin)
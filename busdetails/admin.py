from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import BusDetail

 
class BusDetailAdmin(ImportExportModelAdmin):
    list_display = ('source', 'destination', 'bustype', 'time', 'peak','mid','off')
    list_display_links = ('destination',)
    list_filter = ('source','destination','bustype')
    list_editable = ('source','peak', 'mid','off','time',)
    search_fields = ('source', 'destination', 'bustype', 'time')
    list_per_page = 25

admin.site.register(BusDetail,BusDetailAdmin)


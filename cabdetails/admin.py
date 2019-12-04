from django.contrib import admin

# Register your models here.
from .models import CabDetail
from import_export.admin import ImportExportModelAdmin
class CabDetailAdmin(ImportExportModelAdmin):
    list_display = ('category','pickup', 'destination', 'drop', 'type_of_cab', 'peak','mid','off')
    list_display_links = ('category',)
    list_filter = ('pickup','destination','type_of_cab')
    list_editable = ('pickup','destination','drop','peak', 'mid','off',)
    search_fields = ('destination', 'type_of_cab', 'category')
    list_per_page = 25

admin.site.register(CabDetail,CabDetailAdmin)
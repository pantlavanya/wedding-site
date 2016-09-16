from django.contrib import admin
from images.models import Images
from soul.admin import SoulAdminModel

# Register your models here.
class ImagesAdmin(SoulAdminModel):
    fieldsets = [('Information', {'fields': ['uses']}),
                 ('Upload File', {'fields': ['path']})]
    list_display = ('id', 'original_name', 'modified_name', 'type', 'dimensions', 'size', 'uses','created_at', 'created_by')
    list_filter = ['created_at', 'type']
    search_fields = ['modified_name','type']
    actions = ["export_csv"]


admin.site.register(Images, ImagesAdmin)

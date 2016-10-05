from django.contrib import admin
from django.http import Http404
from soul.utils import export_csv, export_as_json, export_as_xml, export_as_xlsx

# Register your models here.
class SoulAdminModel(admin.ModelAdmin):

    LOOKUP_FIELDS = ['created_at','created_at__gte','created_at__lt']

    list_display = ('created_at','created_by')
    actions = [export_csv, export_as_json, export_as_xml, export_as_xlsx]

    def lookup_allowed(self, key, value):
        if key in SoulAdminModel.LOOKUP_FIELDS:
            return True
        else:
            return False

    def changelist_view(self, request, extra_context=None):
        return super(SoulAdminModel, self).changelist_view(request, extra_context=extra_context)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(SoulAdminModel, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions



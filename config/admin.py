from django.contrib import admin
from config.models import Config
from soul.admin import SoulAdminModel
from django.http import HttpResponseRedirect

# Register your models here.
class ConfigAdmin(SoulAdminModel):
    fieldsets = [('Name (**Note Will Be Capitalized)', {'fields': ['key']}),
                 ('Value', {'fields': ['value']})]
    list_display = ('id', 'key', 'value', 'created_at', 'created_by')
    list_filter = ['created_at']
    actions = ["export_csv"]

    # only index fields are allowed
    LOOKUP_FIELDS = ['id', 'key']
    CONFIG_SEARCH_URL = '/admin/config/search/'

    def lookup_allowed(self, key, value):
        if key in ConfigAdmin.LOOKUP_FIELDS:
            return True
        else:
            return super(ConfigAdmin, self).lookup_allowed(key, value)

    def changelist_view(self, request, extra_context=None):
        get_params = request.GET.keys()
        if 'e' in get_params:
            get_params.remove('e')
        if not get_params:
            return HttpResponseRedirect(ConfigAdmin.CONFIG_SEARCH_URL)
        else:
            return super(ConfigAdmin, self). \
                    changelist_view(request, extra_context=extra_context)

admin.site.register(Config, ConfigAdmin)
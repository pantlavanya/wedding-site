from django.contrib import admin
from models import Member
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from soul.admin import SoulAdminModel


# Register your models here.
class MemberAdmin(SoulAdminModel):
    fieldsets = [('Information', {'fields': ['first_name','middle_name','last_name', 'gender', 'dob', 'marital_status', 'profile_creating_for']}),
                 ('Unique One', {'fields': ['email', 'username', 'contact_number']})]
    list_display = ('id', 'full_member_name' ,'username', 'email', 'created_at', 'created_by')
    list_filter = ['created_at']
    search_fields = ['first_name','middle_name', 'last_name']

    # only index fields are allowed
    LOOKUP_FIELDS = ['id', 'email', 'username', 'contact_number', 'from_date', 'to_date']
    MEMBER_SEARCH_URL = '/admin/member/search/'


    def lookup_allowed(self, key, value):
        if key in MemberAdmin.LOOKUP_FIELDS:
            return True
        else:
            return super(MemberAdmin, self).lookup_allowed(key, value)

    def changelist_view(self, request, extra_context=None):
        get_params = request.GET.keys()
        if 'e' in get_params:
            get_params.remove('e')
        if not get_params:
            return HttpResponseRedirect(MemberAdmin.MEMBER_SEARCH_URL)
        else:
            return super(MemberAdmin, self). \
                    changelist_view(request, extra_context=extra_context)

admin.site.register(Member, MemberAdmin)

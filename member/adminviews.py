from member.models import Member
from django.http import HttpResponse, HttpResponseRedirect
from soul.adminviews import SoulAdminSearchViews
from django.contrib import messages
from django.db.models import Q

class MemberSearchView(SoulAdminSearchViews):
    def get_context_data(self, **kwargs):
        template_data = dict()
        template_data["search_name"] = "Member"
        search_params_list = [
            {'name': 'member_id', 'type': 'text', 'label': 'Id', 'values': '',
             'placeholder':'Enter Member Id', 'class':'vTextField' },
            {'name': 'member_username', 'type': 'text', 'label': 'Username', 'values': '',
             'placeholder': 'Enter Member Username', 'class': 'vTextField'},
            {'name': 'member_email', 'type': 'text', 'label': 'Email', 'values': '',
             'placeholder': 'Enter Member Email', 'class':'vTextField'},
            {'name': 'member_phone_no', 'type': 'text', 'label': 'Phone No', 'values': '',
             'placeholder': 'Enter Member Phone No', 'class':'vTextField'},
            {'name': 'from_date', 'type': 'text', 'label': 'From Date', 'values': '',
             'placeholder': 'Enter Member From Date', 'class':'vDateField'},
            {'name': 'to_date', 'type': 'text', 'label': 'To Date', 'values': '',
             'placeholder': 'Enter Member To Date', 'class':'vDateField'},
        ]
        template_data.update({"search_params_list": search_params_list})

        return template_data

    def post(self, request, *args, **kwargs):
        post_data = request.POST
        cxt_data = self.get_context_data()
        if not post_data["member_id"] and not post_data["member_email"] and not post_data["member_phone_no"]\
            and not post_data["from_date"] and not post_data["to_date"]:
            messages.error(request,"Please provide atleast one input!")
            return self.render_to_response(cxt_data)
        skip = False
        query = Q()
        if post_data["member_id"]:
            skip = True
            get_query = "id=%s&" % post_data["member_id"]
            query &= Q(id=post_data["member_id"])
        if post_data["member_username"] and not skip:
            skip = True
            get_query = "username=%s&" % post_data["member_username"]
            query &= Q(username=post_data["member_username"])
        if post_data["member_email"] and not skip:
            skip = True
            get_query = "email=%s&" % post_data["member_email"]
            query &= Q(email=post_data["member_email"])
        if post_data["member_phone_no"] and not skip:
            skip = True
            get_query = "contact_number=%s&" % post_data["member_phone_no"]
            query &= Q(contact_number=post_data["member_phone_no"])
        """ if post_data["from_date"] and post_data["to_date"]:
            skip = True
            get_query = "id=%s&" % post_data["member_id"]
            filter += "id=%s" % post_data["member_id"] """

        if not Member.objects.filter(query).exists():
            messages.error(request,"No Record Found!")
            return self.render_to_response(cxt_data)

        destination_url = "/admin/member/member/?%s" % get_query
        return HttpResponseRedirect(destination_url)

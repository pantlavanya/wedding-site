from config.models import Config
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from soul.adminviews import SoulAdminSearchViews
import logging

logger = logging.getLogger(__name__)

class ConfigSearchView(SoulAdminSearchViews):
    def get_context_data(self, **kwargs):
        logger.debug('Something went wrong!')
        template_data = dict()
        template_data["search_name"] = "Config"
        search_params_list = [
            {'name': 'config_id', 'type': 'text', 'label': 'Id', 'values': '',
             'placeholder':'Enter Config Id', 'class':'vTextField' },
            {'name': 'config_name', 'type': 'text', 'label': 'Name', 'values': '',
             'placeholder': 'Enter Config Name', 'class': 'vTextField'},
            {'name': 'from_date', 'type': 'text', 'label': 'From Date', 'values': '',
             'placeholder': 'Enter Config From Date', 'class':'vDateField'},
            {'name': 'to_date', 'type': 'text', 'label': 'To Date', 'values': '',
             'placeholder': 'Enter Config To Date', 'class':'vDateField'},
        ]

        template_data.update({'search_params_list': search_params_list})

        return template_data

    def post(self, request, *args, **kwargs):
        post_data = request.POST
        cxt_data = self.get_context_data()
        if not post_data["config_id"] and not post_data["config_name"] and not post_data["from_date"]\
            and not post_data["to_date"]:
            messages.error(request,"Please provide atleast one input!")
            return self.render_to_response(cxt_data)
        skip = False
        query = Q()
        if post_data["config_id"]:
            skip = True
            get_query = "id=%s&" % post_data["config_id"]
            query &= Q(id=post_data["config_id"])
        if post_data["config_name"] and not skip:
            skip = True
            get_query = "name=%s&" % post_data["config_name"]
            query &= Q(name=post_data["config_name"])
        """if post_data["from_date"] and post_data["to_date"]:
            skip = True
            get_query = "id=%s&" % post_data["member_id"]
            filter += "id=%s" % post_data["member_id"]"""

        if not Config.objects.filter(query).exists():
            messages.error(request,"No Record Found!")
            return self.render_to_response(cxt_data)

        destination_url = "/admin/config/config/?%s" % get_query
        return HttpResponseRedirect(destination_url)




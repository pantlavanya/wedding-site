from django.conf.urls import include, url
from django.contrib import admin
from member.adminviews import MemberSearchView

urlpatterns = [
    url(r'^search/$', MemberSearchView.as_view()),
]

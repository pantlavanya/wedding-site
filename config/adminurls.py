from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from config.adminviews import ConfigSearchView

urlpatterns = [
    url(r'^search/$', ConfigSearchView.as_view()),
]



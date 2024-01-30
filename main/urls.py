from django.urls import path 
from .views import *
from django.views.static import serve
from django.urls import re_path
from django.conf import settings

urlpatterns = [
    path("", mainpage, name="index"),
    path("about/", about, name="about"),
    path("conditions/", conditions, name="conditions"),
    path("contact/", contact, name="contact"),
    path("contact/post", Contact.as_view(), name="contact_post"),
    path("portfolio/", portfolio, name="portfolio"),
    path("privacy/", privacy, name="privacy"),
    path("services/", services, name="services"),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

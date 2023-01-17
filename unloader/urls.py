from django.contrib import admin
from django.urls import path
from . import views
# from views import *
# from django.contrib.sitemaps.views import sitemap

# from .sitemaps import StaticViewSitemap
# from . import views

# sitemaps = {
#     'static': StaticViewSitemap,
# }

# app_name='unloadTube'

urlpatterns = [
    path('', views.home, name='home'),
    path('download', views.download, name="download"),
    path('thank-you', views.donations, name="thank-you"),
    path('soon', views.soon, name="soon"),
    # path('fb-astradown', views.url_down, name="fb-astradown")
]
 
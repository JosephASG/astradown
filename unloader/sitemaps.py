from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home', 'download', 'thank-you', 'soon']

    def location(self, item):
        return reverse(item)
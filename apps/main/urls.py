from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', lambda x: HttpResponse("User-Agent: *\nDisallow: /",
                                                mimetype="text/plain")),
)

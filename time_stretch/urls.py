# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',  # noqa
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),
    url(r'^mtg/$',
        TemplateView.as_view(template_name='pages/mtg_charts.html'),
        name="mtg"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    # Your stuff: custom urls go here
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(
        r'^styles/$',
        TemplateView.as_view(template_name='pages/bootstrap_test.html'),
        name='styles'
    ),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url, patterns
from blog import views
from feeds import EntryFeed

urlpatterns = patterns(
    '',
    url(r'^$', views.EntryListView.as_view(), name='index'),
    url(
        r'^entry/(?P<entry_id>[0-9]*)/$',
        views.EntryDetailView.as_view(),
        name='entry'
    ),
    url(r'^rss/$', EntryFeed(), name='entry_feed'),
)

from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'web.views',
    url(r'^$', 'events.index', name='web.index'),
)
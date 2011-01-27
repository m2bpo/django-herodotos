from django.conf.urls.defaults import *

urlpatterns = patterns('herodotos.views',
    url('^(?P<app_label>\w+)/(?P<model>\w+)/(?P<object_pk>\d+)/$', view='object_history', name='herodotos-object-history'),
)

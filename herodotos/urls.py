from django.conf.urls import url

from herodotos.views import object_history

urlpatterns = [
    url('^(?P<app_label>\w+)/(?P<model>\w+)/(?P<object_pk>\d+)/$', view=object_history, name='herodotos-object-history'),
]


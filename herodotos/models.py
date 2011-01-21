from datetime import datetime

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from toolbox.choices import pick_choice


class Event(models.Model):
    date = models.DateTimeField(_('date'), default=datetime.now)
    user = models.ForeignKey(User, verbose_name=_('user'))
    action = models.PositiveIntegerField(_('action'), max_length=20)
    comment = models.TextField(_('comment'), blank=True)
    
    # generic FK
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    
    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
    
    def get_action_display(self):
        pass # TODO


class HerodotosEnabledMixin(object):
    history = generic.GenericRelation(Event)
    
    def record(self, **kwargs):
        e = Event(content_object=self, **kwargs)
        e.save()

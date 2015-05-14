from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from herodotos.actions import get_action_list_for_contenttype
from toolbox.choices import pick_choice


class Event(models.Model):
    date = models.DateTimeField(_('date'), default=datetime.now)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='history')
    action = models.PositiveIntegerField(_('action'))
    comment = models.TextField(_('comment'), blank=True)
    
    # generic FK
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    
    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ('date',)
    
    def get_action_display(self):
        action_list = get_action_list_for_contenttype(self.content_type)
        return pick_choice(action_list, self.action)


class HerodotosEnabledMixin(object):
    @property
    def history(self):
        contenttype = ContentType.objects.get_for_model(self)
        return Event.objects.filter(content_type__pk=contenttype.pk, object_id=self.pk)
    
    def record(self, **kwargs):
        e = Event(content_object=self, **kwargs)
        e.save()
    
    def get_history_url(self):
        from django.core.urlresolvers import reverse
        app_label = self._meta.app_label
        model = self._meta.object_name.lower()        
        return reverse('herodotos-object-history', args=[app_label, model, self.pk])

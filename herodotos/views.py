from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

class HerodotosEnabledMixin(object):
    action_id = None
    
    def record(self, comment='', user=None):
        if user is None:
            user = self.request.user
        if self.action_id is not None:
            self.object.record(action=self.action_id, comment=comment, user=user)


class ObjectHistoryView(ListView):
    """A generic view to display the history of an object."""
    
    def get_queryset(self):
        contenttype = get_object_or_404(ContentType,
                                            app_label=self.kwargs['app_label'],
                                            model=self.kwargs['model'])
        object = get_object_or_404(contenttype.model_class(), pk=self.kwargs['object_pk'])
        
        self.contenttype, self.object = contenttype, object
        return object.history.all()
    
    
    def get_context_data(self, **kwargs):
        context = super(ObjectHistoryView, self).get_context_data(**kwargs)
        context.update({
            'object': self.object,
            'contenttype': self.contenttype
        })
        
        return context

object_history = ObjectHistoryView.as_view(template_name='herodotos/object_history.html')

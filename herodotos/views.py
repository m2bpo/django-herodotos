from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

def object_history(request, app_label, model, object_pk):
    contenttype = get_object_or_404(ContentType, app_label=app_label, model=model)
    object = get_object_or_404(contenttype.model_class(), pk=object_pk)
    
    return object_list(request,
        queryset=object.history.all(),
        template_name='herodotos/object_history.html',
        extra_context={
            'object': object,
            'contenttype': contenttype,
        })

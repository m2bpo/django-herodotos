from django.utils.translation import ugettext_lazy as _

CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4

ACTIONS = (
    (CREATE, _('create')),
    (READ, _('read')),
    (UPDATE, _('update')),
    (DELETE, _('delete')),
)

def get_action_list_for_contenttype(contenttype):
    from herodotos import _cache
    try:
        return _cache[contenttype.pk]
    except KeyError:
        try:
            actions = contenttype.model_class().Herodotos.ACTIONS
        except AttributeError:
            actions = ACTIONS
    _cache[contenttype.pk] = actions
    return actions

from django import template

register = template.Library()

@register.assignment_tag
def get_last(action, history):
    """{% get_last ACTION HISTORY as FOO %}"""
    history = history.order_by('-date').filter(action=action)
    return history[0]


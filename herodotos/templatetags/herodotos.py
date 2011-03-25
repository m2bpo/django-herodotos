from django import template

register = template.Library()

class GetLastNode(template.Node):
    def __init__(self, history, action, varname):
        self.history = template.Variable(history)
        self.action = template.Variable(action)
        self.varname = varname
    
    
    def render(self, context):
        history = self.history.resolve(context)
        action = self.action.resolve(context)
        history = history.order_by('-date').filter(action=action)
        
        try:
            context[self.varname] = history[0]
        except IndexError:
            context[self.varname] = None
        return ''


@register.tag
def get_last(parser, token):
    """{% get_last ACTION from HISTORY as FOO %}"""
    content = token.split_contents()
    action = content[1]
    history = content[3]
    varname = content[5]
    
    return GetLastNode(history, action, varname)


from pyramid.view import view_config


@view_config(route_name='sellings',
             renderer='zello_backend:templates/view_sellings.jinja2')
def sellings_view(request):
    return {}


@view_config(route_name='sellings_action', match_param='action=create',
             renderer='zello_backend:templates/edit_sellings.jinja2')
def sellings_create(request):
    return {}


@view_config(route_name='sellings_action', match_param='action=edit',
             renderer='zello_backend:templates/edit_sellings.jinja2')
def sellings_update(request):
    return {}

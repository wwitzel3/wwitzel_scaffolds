from pyramid.view import view_config

@view_config(route_name='index', renderer='default/index.mako')
def index(request):
    return dict()

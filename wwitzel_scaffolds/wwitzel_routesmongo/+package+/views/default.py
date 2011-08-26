from pyramid.view import view_config

@view_config(route_name='index', render='default/index.mako')
def index(request):
    return dict()

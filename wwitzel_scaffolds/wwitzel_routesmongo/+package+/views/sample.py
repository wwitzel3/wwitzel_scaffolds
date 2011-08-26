from pyramid.view import view_config
import {{package}}.models as M

@view_config(route_name='sample', render='sample/index.mako')
def sample(request):
    return dict(
        samples=request.db.query(M.Sample)
    )
    
@view_config(route_name='sample_instance', render='sample/instance.mako')
def sample_instance(request, id):
    return dict(
        sample=request.db.query(M.Sample).get(id)
    )
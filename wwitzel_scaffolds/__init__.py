import os
from paste.util.template import paste_script_template_renderer
from pyramid.scaffolds import PyramidTemplate

class WRoutesAlchemyTemplate(PyramidTemplate):
    _template_dir = 'wwitzel_routesalchemy'
    summary = 'Pyramid SQLalchemy project using Mako templates and url dispatch (no traversal)'
    #template_renderer = staticmethod(paste_script_template_renderer)

class WRoutesMongoTemplate(PyramidTemplate):
    _template_dir = 'wwitzel_routespymongo'
    summary = 'Pyramid MongoDB project using Mako templates and url dispatch (no traversal)'
    #template_renderer = staticmethod(paste_script_template_renderer)

from pyramid.scaffolds import PyramidTemplate

class WRoutesMongoTemplate(PyramidTemplate):
    _template_dir = 'ww3_pymongo'
    summary = 'Pyramid MongoDB project using Mako templates and url dispatch (no traversal)'
    #template_renderer = staticmethod(paste_script_template_renderer)

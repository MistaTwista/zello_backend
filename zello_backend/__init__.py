from pyramid.config import Configurator
from .utils.jsonhelpers import custom_json_renderer


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('.cors')
    config.add_cors_preflight_handler()
    config.add_renderer('json', custom_json_renderer())
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()

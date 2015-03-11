from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery
from arche.interfaces import IViewInitializedEvent
from arche.interfaces import IBaseView
from arche.fanstatic_lib import main_css


voteit_site_lib = Library('voteit_site', 'static')
voteit_site_css = Resource(voteit_site_lib, 'css/main.css', depends = (main_css,))

def include_resources(view, event):
    voteit_site_css.need()

def includeme(config):
    config.add_subscriber(include_resources, [IBaseView, IViewInitializedEvent])

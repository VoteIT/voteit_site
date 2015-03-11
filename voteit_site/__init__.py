
def includeme(config):
    config.include('.fanstatic_lib')
    config.override_asset(to_override='arche:templates/',
                          override_with='voteit_site:templates/overrides/')
    cache_max_age = int(config.registry.settings.get('arche.cache_max_age', 60*60*24))
    config.add_static_view('voteit_site_static', 'voteit_site:static', cache_max_age = cache_max_age)

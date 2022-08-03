from middleware import db, index, user_profile, hero, hero_add, hero_update
from flask import jsonify

def initiatise_routes(app):
    if app:
        app.add_url_rule('/api/hallo/', 'index', index)  # endpoint URL, "function", function.
        app.add_url_rule('/api/db/', 'db', db)
        app.add_url_rule('/', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
        app.add_url_rule('/api/profile/<id>/', 'user_profile', user_profile)
        app.add_url_rule('/api/hero/', 'hero', hero)
        app.add_url_rule('/api/hero/', 'hero_add', hero_add, methods=['POST'])
        app.add_url_rule('/api/hero/', 'hero_update', hero_update, methods=['PUT'])
    return None

def list_routes(app):
    routes = []
    for route in app.url_map.iter_rules():
        routes.append({'Route': str(route),
                       'Endpoint': route.endpoint,
                       'Methods': list(route.methods)
                       })


    return jsonify({"Routes" : routes, "Total" : len(routes)})
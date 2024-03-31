#!/usr/bin/python3
"""Index module"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """Return status OK"""
    return jsonify({'status': 'OK'})

@app_views.route('/stats')
def stats():
    """Return the number of each object by type."""
    stats_data = {}
    models = ["User", "State", "City", "Amenity", "Place", "Review"]
    for model in models:
        count = storage.count(model)
        stats_data[model] = count
    return jsonify(stats_data)

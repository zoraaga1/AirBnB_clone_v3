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
    models_available = {
        "User": "users",
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states"
    }

    stats_data = {}
    for model, table_name in models_available.items():
        count = storage.count(table_name)
        stats_data[model.lower() + "_count"] = count
    return jsonify(stats_data)

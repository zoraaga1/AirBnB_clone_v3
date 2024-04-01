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

    stats = {}
    for cls in models_available.keys():
        stats[models_available[cls]] = storage.count(cls)
    return jsonify(stats)

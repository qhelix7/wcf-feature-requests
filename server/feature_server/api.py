from flask import Blueprint, current_app, jsonify

from feature_server import db, models

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/client', methods=('GET', ))
def get_clients():
    clients = models.Client.query.all()
    data = {
        "clients": [
            {"id": client.id, "name": client.name}
            for client in clients
        ]
    }
    return jsonify(data)

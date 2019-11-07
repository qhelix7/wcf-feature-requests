from datetime import datetime

from flask import Blueprint, current_app, jsonify, request

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


@api.route('/feature-request', methods=('GET', ))
def get_feature_requests():
    feature_requests = models.FeatureRequest.query.all()
    data = {
        "feature_requests": [fr.to_dict() for fr in feature_requests]
    }
    return jsonify(data)


@api.route('/feature-request', methods=('POST', ))
def post_feature_request():
    # TODO: verify inputs and report errors
    data = request.get_json()
    
    feature = models.FeatureRequest(
        title=data["title"],
        description=data.get("description", ""),
        client_id=data["client_id"],
        priority=data["priority"],
        target_date=datetime.fromisoformat(data["target_date"]),
    )
    db.session.add(feature)
    db.session.commit()

    return jsonify(feature.to_dict())


@api.route('/feature-request/<id_>', methods=('GET', ))
def get_feature_request(id_):
    # TODO: handle 404
    feature_requests = models.FeatureRequest.query.filter_by(id=id_).one()
    return jsonify(feature_requests.to_dict())

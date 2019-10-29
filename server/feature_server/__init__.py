import os

from flask import Flask, send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

from feature_server import config

app = None
db = SQLAlchemy()


def load_models():
    from feature_server import models


load_models()


def create_app():
    global app
    from feature_server.api import api
    app = Flask(__name__, static_url_path='', static_folder=config.DIST_DIR)
    
    app.config.from_object(config)

    # Bind the app and database
    db.init_app(app)

    # Fix CORS issue when running behind a reverse-proxy
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.register_blueprint(api, url_prefix='/api')

    @app.route('/')
    def index():
        return send_file(os.path.join(app.config['DIST_DIR'], 'index.html'))

    @app.route('/<path:path>')
    def root(path):
        return send_from_directory(app.config['DIST_DIR'], path)

    return app

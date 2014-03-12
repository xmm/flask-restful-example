#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
import flask_restful

#from api.database import db
from api.v1 import api_v1, api_v1_bp, API_VERSION_V1
from api.v2 import api_v2, api_v2_bp, API_VERSION_V2


def create_app(environment="Development"):
    app = Flask(__name__)
    app.config.from_object('api.config.{}'.format(environment))

    app.register_blueprint(
        api_v1_bp,
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['URL_PREFIX'],
            version=API_VERSION_V1))

    app.register_blueprint(
        api_v2_bp,
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['URL_PREFIX'],
            version=API_VERSION_V2))

    return app

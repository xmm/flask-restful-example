# -*- coding: utf-8 -*-
'''
Copyright (c) 2013
@author: Marat Khayrullin <xmm.dev@gmail.com>
'''

from flask import Flask, Blueprint
import flask_restful


API_VERSION_V2=2
API_VERSION=API_VERSION_V2

api_v2_bp = Blueprint('api_v2', __name__)
api_v2 = flask_restful.Api(api_v2_bp)


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {
            'HELLO': 'WORLD',
            'VERSION': API_VERSION,
            }


api_v2.add_resource(HelloWorld, '/helloworld')

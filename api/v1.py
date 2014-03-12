# -*- coding: utf-8 -*-
'''
Copyright (c) 2013
@author: Marat Khayrullin <xmm.dev@gmail.com>
'''

from flask import Flask, Blueprint
import flask_restful


API_VERSION_V1=1
API_VERSION=API_VERSION_V1

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = flask_restful.Api(api_v1_bp)


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {
            'hello': 'world',
            'version': API_VERSION,
            }


api_v1.add_resource(HelloWorld, '/helloworld')

#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path


class Config(object):
    DEBUG = False
    PORT = 5000
    HOST = "0.0.0.0"
    URL_PREFIX = '/api'
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    TEMPLATE_FOLDER = path.join(PROJECT_ROOT, 'templates')


class Development(Config):
    DEBUG = True


class Production(Config):
    SQLALCHEMY_ECHO = False
    MYSQL_DATABASE_HOST = '10.0.0.1'
    MYSQL_DATABASE_DB = 'db'
    MYSQL_DATABASE_USER = 'user'
    MYSQL_DATABASE_PASSWORD = 'password'


class Testing(Config):
    SECRET_KEY = "2147d2df-759b-40ac-8013-f6154110a7d0"
    TESTING = True

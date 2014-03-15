#!/usr/bin/python
# -*- coding: utf-8 -*-

from api import create_app
import unittest
import flask
import json


class APIV1TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(environment="Testing")

    def test_hello_version(self):
        data = json.loads(self.app.test_client().get('/api/v1/helloworld').data)
        assert data.get('version') == 1
        assert data.get('hello') == 'world'


if __name__ == '__main__':
    unittest.main()

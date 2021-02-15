from flask_testing import TestCase
from flask import Flask
import requests
import json
import src.password_api

class app_password_test(TestCase):

    def create_app(self):
        app = src.password_api.create_app()
        app.config['TESTING'] = True
        return app

    def test_check_server_up(self):
        response = self.client.post("/")
        self.assertStatus(response, 404)

    def test_check_endpoint(self):
        response = self.client.post("/verifypassword")
        self.assertStatus(response, 200)

    def test_check_positive_password_response(self):
        response = self.client.post("/verifypassword", data="Daniel1@3", headers={'Content-Type': 'application/text'})
        self.assertStatus(response, 200)
        self.assertTrue(json.loads(response.data))

    def test_check_negative_password_response(self):
        response = self.client.post("/verifypassword", data="Daniela1@", headers={'Content-Type': 'application/text'})
        self.assertStatus(response, 200)
        self.assertFalse(json.loads(response.data))

import os

from flask import render_template, make_response, send_from_directory
from flask_restful import Resource
from flask_restful import current_app as app


class Index(Resource):
    @staticmethod
    def get():
        headers = {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*'
        }

        html = os.path.join('index.html')
        return make_response(
            render_template(html), 200, headers)


class Favicon(Resource):
    @staticmethod
    def get():
        return send_from_directory(
            os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

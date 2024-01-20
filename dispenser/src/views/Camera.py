from flask_restful import Resource, reqparse
from controllers.Camera import Camera


class Capture(Resource):
    @staticmethod
    def get():
        try:
            picture = Camera().capture()

            response = {
                'message': {
                    'status': 'SUCCESS',
                    'picture': picture.base64string
                }
            }
            return response, 200
        except Exception as e:
            response = {
                'message': {
                    'status': 'ERROR',
                    'response': str(e)
                }
            }
            print(e)
            return response, 500


class Device(Resource):
    @staticmethod
    def get():
        try:
            dev = Camera().get_camera()

            response = {
                'message': {
                    'status': 'SUCCESS',
                    'device': dev
                }
            }
            return response, 200
        except Exception as e:
            response = {
                'message': {
                    'status': 'ERROR',
                    'response': str(e)
                }
            }
            print(e)
            return response, 500

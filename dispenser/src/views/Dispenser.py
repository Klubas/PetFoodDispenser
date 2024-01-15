from flask_restful import Resource, reqparse

from config.Parameters import OPEN_SECONDS, OPEN_ANGLE, CLOSE_ANGLE
from controllers.Dispenser import Dispenser


class Open(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('open_angle', type=float, required=False, location='args', default=OPEN_ANGLE)

        args = parser.parse_args()

        try:

            Dispenser().open(open_angle=args.open_angle)

            response = {
                'message': {
                    'status': 'SUCCESS',
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


class Close(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('close_angle', type=float, required=False, location='args', default=CLOSE_ANGLE)

        args = parser.parse_args()

        try:

            Dispenser().close(close_angle=args.close_angle)

            response = {
                'message': {
                    'status': 'SUCCESS',
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


class Feed(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('open_angle', type=float, required=False, location='args', default=OPEN_ANGLE)
        parser.add_argument('close_angle', type=float, required=False, location='args', default=CLOSE_ANGLE)
        parser.add_argument('open_seconds', type=float, required=False, location='args', default=OPEN_SECONDS)

        args = parser.parse_args()

        try:
            status, picture = Dispenser().dispense_food(open_angle=args.open_angle,
                                                        close_angle=args.close_angle,
                                                        open_seconds=args.open_seconds)

            response = {
                'message': {
                    'status': 'SUCCESS',
                    'picture': picture
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

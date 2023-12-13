from flask_restful import Resource, reqparse

from config.Parameters import OPEN_SECONDS, OPEN_ANGLE, CLOSE_ANGLE
from controllers.DispenserController import DispenserController as Dispenser


class FoodDispenser(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('open_angle', type=float, required=False, location='args', default=OPEN_ANGLE)
        parser.add_argument('close_angle', type=float, required=False, location='args', default=CLOSE_ANGLE)
        parser.add_argument('open_seconds', type=float, required=False, location='args', default=OPEN_SECONDS)

        args = parser.parse_args()

        try:
            Dispenser().dispense_food(open_angle=args.open_angle,
                                      close_angle=args.close_angle,
                                      open_seconds=args.open_seconds)

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

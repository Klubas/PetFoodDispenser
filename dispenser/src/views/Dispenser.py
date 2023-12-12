from flask_restful import Resource, reqparse

from src.controllers.DispenserController import DispenserController as Dispenser
from src.config.Parameters import OPEN_SECONDS, OPEN_ANGLE, CLOSE_ANGLE


class FoodDispenser(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('open_angle', type=str, required=False, location='args', default=OPEN_ANGLE)
        parser.add_argument('close_angle', type=str, required=False, location='args', default=CLOSE_ANGLE)
        parser.add_argument('open_seconds', type=str, required=False, location='args', default=OPEN_SECONDS)

        args = parser.parse_args()
        
        try:
            status = Dispenser().dispense_food(open_angle=args.open_angle
                                           , close_angle=args.close_angle
                                           , open_seconds=args.open_seconds)
            return 'Success', 200
        except Exception as e:
            return 'Error', 401
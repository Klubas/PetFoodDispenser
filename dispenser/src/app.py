import argparse
from datetime import datetime

from flask import Flask, send_from_directory
from flask_restful import Api, Resource
from flask_cors import CORS

from src.views.Index import Index, Favicon
from src.views.Dispenser import FoodDispenser

from src.config.Parameters import DEBUG, HOSTNAME, PORT, EXPLAIN_TEMPLATE_LOADING, DISABLE_ERROR_BUNDLE


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['EXPLAIN_TEMPLATE_LOADING'] = EXPLAIN_TEMPLATE_LOADING
app.config['BUNDLE_ERRORS']            = not DISABLE_ERROR_BUNDLE

# add resources
api = Api(app)
api.add_resource(Favicon, '/favicon.ico')
api.add_resource(Index, '/')
api.add_resource(FoodDispenser, '/api/dispenser/feed')


def runApp():
    parser = argparse.ArgumentParser(
        description="PetFoodDispenser"
    )

    parser.add_argument(
        '--hostname'
        , metavar='hostname:port'
        , type=str
        , help="hostname and port number for the server in the format: <hostname>:<port>"
        , nargs="?"
        , required=False
    )

    parser.add_argument(
        '--debug'
        , help="Run in debug mode"
        , action='store_true'
    )

    args = parser.parse_args()
            
    if args.hostname:
        hostname = args.hostname.split(":")
        host = hostname[0]
        port = int(hostname[1])
    else:
        host = HOSTNAME
        port = PORT

    if args.debug:
        debug = args.debug
    else:
        debug = DEBUG

    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
   try:
      runApp()
   except (KeyboardInterrupt, SystemExit):
      print("Exiting APP...")
from os import getenv

#API
HOSTNAME                    = getenv('HOSTNAME'                 , default='0.0.0.0')
PORT                        = getenv('PORT'                     , default='5000')
EXPLAIN_TEMPLATE_LOADING    = getenv('EXPLAIN_TEMPLATE_LOADING' , default='False')
DISABLE_ERROR_BUNDLE        = getenv('DISABLE_ERROR_BUNDLE'     , default='True')
DEBUG                       = True if \
                                getenv('DEBUG'                  , default=0) == "1" else False

#SERVO
OPEN_SECONDS   = float(getenv('OPEN_SECONDS'  , default=2))
OPEN_ANGLE     = float(getenv('OPEN_ANGLE'    , default=30))
CLOSE_ANGLE    = float(getenv('CLOSE_ANGLE'   , default=0))
SCHEDULE_TIMES =       getenv('SCHEDULE_TIMES', default="06:00,09:00,12:00,15:00,18:00,21:00").split(',')
TZ             =       getenv('TZ'            , default="America/Sao_Paulo") 

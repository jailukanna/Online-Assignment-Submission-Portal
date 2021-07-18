from argparse import ArgumentParser
from logging.config import dictConfig
from sys import stdout

from rfxcom import protocol

from home.collect.handlers import RecordingHander, LoggingHandler
from home.collect.loop import collect
from home.ts import syncdb

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)-8s %(name)-35s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': stdout,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'rfxcom': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'home': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    },
}


def run():
    dictConfig(LOGGING)

    elec_handler = RecordingHander({
        'electricity': 'current_watts',
        'total_watts': 'total_watts'
    })

    temp_humidity_handler = RecordingHander({
        'temperature': 'temperature',
        'humidity': 'humidity'
    })

    logging_handler = LoggingHandler()

    syncdb()

    parser = ArgumentParser(description='.')
    parser.add_argument('--device')

    args = parser.parse_args()
    collect(args.device, {
        protocol.Status: logging_handler,
        protocol.Elec: elec_handler,
        protocol.TempHumidity: temp_humidity_handler,
        '*': logging_handler,
    })

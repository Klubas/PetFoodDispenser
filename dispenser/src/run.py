"""
Service must be start by this module
"""
import signal
import sys
from threading import Thread

from app import runapp, app
from scheduler import run_schedules


def signal_handler(signal, frame):
    print("Killing threads and exiting...")
    sys.exit(0)


app = app


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    t1 = Thread(target=run_schedules)
    t1.daemon = True
    t1.start()

    t2 = Thread(target=runapp)
    t2.daemon = True
    t2.start()

    t1.join()
    t2.join()
else:
    signal.signal(signal.SIGINT, signal_handler)

    t1 = Thread(target=run_schedules)
    t1.daemon = True
    t1.start()

    # t1.join()

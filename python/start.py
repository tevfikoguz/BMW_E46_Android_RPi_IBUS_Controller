#!/usr/bin/env python
import globals
from ibus_service.ibus import IBUSService
from android_service.bt import AndroidBluetoothService
import signal
import sys
import time


def signal_handler_quit(signal, frame):
    """
    Invoked when 'Ctrl+C' is pressed
    """
    print "Stopping services..."
    if globals.ibus_service is not None:
        globals.ibus_service.destroy()
    if globals.android_service is not None:
        globals.android_service.destroy()
    sys.exit(0)


def start_services():
    """
    Main method of the Rasperry Pi service(s)
    """
    print "BMW IBUS/RasperryPi/Android Controller"
    print "Starting services..."
    signal.signal(signal.SIGINT, signal_handler_quit)

    # initialize ibus and android services
    try:
        print "Initializing IBUS service...."
        globals.ibus_service = IBUSService()
        print "Initializing BLUETOOTH service...."
        globals.android_service = AndroidBluetoothService()
        print "All services running..."
    except Exception as e:
        print "Error: " + e.message + "\n" + "Failed to start, trying again in 5 seconds..."
        time.sleep(5)
        print "Restarting now...\n"
        start_services()
        return

    # until "Ctrl-C" is pressed
    while True:
        time.sleep(1)

# start RPi services
start_services()
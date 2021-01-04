#!/usr/bin/python3

import psutil
import paho.mqtt.publish as publish
import sys
import getopt
import json

# MQTT topic to publish the message to
TOPIC="laptop/battery"

# unique MQTT client id
CLIENT_ID="dell-laptop"

def main(argv):
    broker_address = ""
    
    try:
        opts, args = getopt.getopt(argv,"b:")
    except getopt.GetoptError:
        print("battery-status-win.py -b <broker-address>")
        sys.exit(1)

    # parse commandline arguments
    for opt, arg in opts:
        if opt == "-b":
          broker_address = arg

    # publish battery status
    battery = psutil.sensors_battery()
    if ((battery.percent < 20 and not battery.power_plugged) or battery.percent == 100):
        payload = dict()
        payload['POWER_SUPPLY_CAPACITY'] = str(battery.percent)
        payload['POWER_SUPPLY_STATUS'] = str(battery.power_plugged)

        encoded_payload = json.dumps(payload)
        publish.single(topic=TOPIC, payload=encoded_payload, hostname=broker_address, client_id=CLIENT_ID)

if __name__ == '__main__':
    main(sys.argv[1:])

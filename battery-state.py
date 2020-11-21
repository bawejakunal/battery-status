#!/usr/bin/python3

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
        print("battery-status.py -b <broker-address>")
        sys.exit(1)

    # parse commandline arguments
    for opt, arg in opts:
        if opt == "-b":
          broker_address = arg

    # publish battery status
    with open("/sys/class/power_supply/BAT0/uevent", "r") as handle:
        lines = handle.readlines()

        payload = dict()
        for line in lines:
            key, val = line.strip().split('=')
            payload[key] = val

        capacity = int(payload['POWER_SUPPLY_CAPACITY'])
        power_status = payload['POWER_SUPPLY_STATUS'].lower()

        if (capacity < 20 and power_status != 'charging') or capacity == 100:
            encoded_payload = json.dumps(payload)
            publish.single(topic=TOPIC, payload=encoded_payload, hostname=broker_address, client_id=CLIENT_ID)

if __name__ == '__main__':
    main(sys.argv[1:])

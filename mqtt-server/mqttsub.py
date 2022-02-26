#!/usr/bin/env python3

"""
Garden automation, subscribing to topics, reading & handling messages.
"""
import time
import json
import paho.mqtt.client as mqtt
import dbconnection as db

from configparser import ConfigParser
config = ConfigParser()
config.read('settings.ini')

client = mqtt.Client(config['device']['name'], False)

# The callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    for device in config['client']['name'].split(', '):
        client.subscribe([(device + "/sensors", 1)])
        client.subscribe([(device + "/actuators", 1)])
        client.subscribe([(device + "/system", 1)])
        print('subscribed to device: ' + device)

def on_message(client, userdata, msg):
    print('msg!')
    msg_decode=str(msg.payload.decode("utf-8","ignore"))
    try:
        msg_in=json.loads(msg_decode)

        for device in config['client']['name'].split(', '):
            if msg.topic == device + "/sensors":
                print(device + '/sensors ' + json.dumps(msg_in))
                db.write('sensors', device, msg_decode)

            elif msg.topic == device + "/actuators":
                print(device + '/actuators ' + json.dumps(msg_in))
                db.write('actuators', device, msg_decode)

            elif msg.topic == device + "/system":
                print(device + '/system ' + json.dumps(msg_in))
                db.write('system', device, msg_decode)


    except Exception as e:
        print(e)

def get_messages():
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect('192.168.1.100', 1883, 60)
        client.loop_start()
        time.sleep(10)
        client.loop_stop()
    except Exception as e:
        print(e)

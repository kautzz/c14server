# c14server

off grid garden automation
server side

WIP

## mqtt-server

Listen to mqtt channels and write device, sensor, actuator and event data to couchDB

## www

Webserver running webinterface for accessing device, sensor, actuator and event data of the database. Can also send commands and change settings of devices over mqtt.

# couchDB

Following this guide to install on raspberry pi

https://github.com/jguillod/couchdb-on-raspberry-pi

* needed to do this to successfully build couchDB on pi: https://raspberrypi.stackexchange.com/a/113698

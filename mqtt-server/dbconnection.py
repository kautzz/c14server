
#!/usr/bin/env python3

import os
import sys
import sqlite3

def get_connection():
	if os.path.isfile('garden.db'):
		conn = sqlite3.connect('garden.db')
		print ("connected to garden.db", file=sys.stderr)
	else:
		conn = sqlite3.connect('database.db')
		print ("garden.db not found", file=sys.stderr)
	conn.row_factory = sqlite3.Row
	return conn

def write(table, device, reading):
	conn = get_connection()
	conn.execute('INSERT INTO ' + table + ' (device, reading) VALUES (?, ?)', (device, reading))
	conn.commit()
	conn.close()

def get_last_sensor_data(device):
	conn = get_connection()
	post = conn.execute('SELECT * FROM sensors WHERE device = ?', (device,)).fetchone()
	conn.close()

def get_last_data():
	conn = get_connection()
	result = conn.execute('SELECT * FROM sensors ORDER BY id DESC LIMIT 1').fetchone()
	for row in result:
		print(row)
	result = conn.execute('SELECT * FROM actuators ORDER BY id DESC LIMIT 1').fetchone()
	for row in result:
		print(row)
	result = conn.execute('SELECT * FROM events ORDER BY id DESC LIMIT 1').fetchone()
	for row in result:
		print(row)



	conn.close()

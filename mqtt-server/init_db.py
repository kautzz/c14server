#!/usr/bin/env python3

import sqlite3
import secrets

connection = sqlite3.connect('garden.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO sensors (device, reading) VALUES (?, ?)",
            ('init', '{"sensors": "init"}')
            )

cur.execute("INSERT INTO actuators (device, reading) VALUES (?, ?)",
            ('init', '{"actuators": "init"}')
            )

cur.execute("INSERT INTO events (device, reading) VALUES (?, ?)",
            ('init', '{"system": "init"}')
            )

cur.execute("INSERT INTO images (filename, extension) VALUES (?, ?)",
            ('init', 'jpg')
            )

connection.commit()
connection.close()

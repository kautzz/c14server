#!/usr/bin/env python3

import datetime
import mqttsub
import dbconnection as db

def main():
    lastRead = datetime.datetime.now().timestamp() * -1

    try:
        while True:
            if 5 <= datetime.datetime.now().timestamp() - lastRead:
                db.get_last_data()
                lastRead = datetime.datetime.now().timestamp()

            mqttsub.get_messages()

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

print('')
print('[ ☑ End Of Program ]')

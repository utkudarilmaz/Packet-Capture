from scapy.all import *
from influxdb import InfluxDBClient
import os
import time
import datetime

try:
    client = InfluxDBClient(host='192.168.1.240', port=8086, username='test', password='123456')
    client.switch_database('test')
except e:
    print(e)
    exit()

try:
    os.chdir("/var/log/tshark")
except FileNotFoundError:
    try:
        os.mkdir("/var/log/tshark")
        os.chdir("/var/log/tshark")
    except PermissionError:
        print(k)
        exit()

try:
    os.chdir("/var/log/tshark")
    capture = "tshark -O icmp -T json -w log.cap -b duration:30 &"
    os.system(capture)
except e:
    print(e)
    exit()

host = {}

while True:

    files = os.listdir(path='/var/log/tshark/')
    files.sort()

    if len(files) > 2:
        file = files[0]

        a = rdpcap(file)

        for i in range(len(a)):
            try:
                if a[i].type == 2048:

                    source = a[i][IP].src
                    target = a[i][IP].dst

                    header = "logs"

                    try:
                        if a[i][ICMP].type == 8:
                             log = [{
                                 'measurement': header,
                                 'tags': {
                                     'source': source,
                                     'target': target,
                                 },
                                 'time': datetime.datetime.utcnow(),
                                 "fields": {
                                     "value": float(1),
                                 },
                             }]
                             client.write_points(log)
                        else:
                            continue
                    except IndexError:
                        continue
                    else:
                        continue
                else:
                    continue
            except AttributeError as e:
                continue
            else:
                continue
        os.remove(file)
    else:
        continue

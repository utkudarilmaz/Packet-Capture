from scapy.all import *
from influxdb import InfluxDBClient
import os
import time

try:
    client = InfluxDBClient(host='172.17.0.3', port=8086, username='test', password='123456')
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

# try:
#     os.chdir("/var/log/tshark")
#     capture = "tshark -O icmp -T json -w log.cap -b duration:30 &"
#     os.system(capture)
# except e:
#     print(e)
#     exit()

host = {}

while True:


    files = os.listdir()
    files.sort()

    if len(files) > 1:
        file = files[0]

        logs = []
        target = ""

        a = rdpcap(file)

        for i in range(len(a)):

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
                             "fields": {
                                 "value": float(1),
                             }
                             # 'time': a[]
                         }]
                         client.write_points(log)
                    else:
                        continue
                except IndexError:
                    continue
            else:
                continue
        os.remove(file)
    else:
        continue


# while True:
#
#
#     files = os.listdir()
#     files.sort()
#
#     if len(files) > 1:
#         file = files[0]
#
#         a = rdpcap(file)
#
#         for i in range(len(a)):
#
#             if a[i].type == 2048:
#
#                 source = a[i][IP].src
#
#                 if a[i][ICMP].type == 8:
                    # if source in host:
                    #     host[source] = host[source] + 1
                    # else :
                    #     host[source] = 1
#                 else:
#                     continue
#             else:
#                 continue
#
#         print(host)
#         os.remove(file)
#
#     else:
#         continue

import json
import socket
import struct

def addressInNetwork(ip, net):
    "Is an address in a network"
    ipaddr = struct.unpack('L', socket.inet_aton(ip))[0]
    netaddr, bits = net.split('/')
    netmask = struct.unpack('L', socket.inet_aton(netaddr))[0] & ((2L << int(bits)-1) - 1)
    return ipaddr & netmask == netmask

class Alert(object):
    alert_type = None
    alert = None
    origin_ip = None
    destination_ip = None
    alert_result = None

    def __init__(self, alert_type=None, alert=None, origin_ip=None, destination_ip=None, alert_result=None):
        self.alert_type = alert_type
        self.alert = alert
        self.origin_ip = origin_ip
        self.destination_ip = destination_ip
        self.alert_result = alert_result

    def __repr__(self):
        return str(self.alert_type) + ' : ' + str(self.alert)

    def alert_from_json(self, alert_json):
        dct = json.loads(alert_json)
        for key in dct:
            setattr(self, key, dct[key])
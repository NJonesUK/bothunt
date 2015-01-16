import ipaddr
import struct

def addressInNetwork(ip, net):
    "Is an address in a network"
    return ipaddr.IPv4Address(ip) in ipaddr.IPv4Network(net)
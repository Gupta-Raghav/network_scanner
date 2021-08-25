#! /usr/bin/env python3

import scapy.all as scapy


def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet_broadcast = broadcast/arp_packet
    answered, unanswered = scapy.srp(arp_packet_broadcast, timeout=1)
    print(answered.summary())

scan("192.168.68.0/24")
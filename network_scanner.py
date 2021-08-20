#! /usr/bin/env python3

import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)

scan("192.168.68.0/24")
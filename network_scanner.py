#! /usr/bin/env python3
import argparse

import scapy.all as scapy
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="This is the Target IP/range of IP addresses")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify the IP address or the Range of IP Address that you want to scan")
    else:
        return options


def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet_broadcast = broadcast/arp_packet
    answered_list = scapy.srp(arp_packet_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for client in answered_list:
        client_dict = {"ip": client[1].psrc, "MAC": client[1].psrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(clients_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------------------------------------------")
    for end_devices in clients_list:
        print(end_devices["ip"] + "\t\t" + end_devices["MAC"])


options = get_args()
scan_result = scan(options.target)
print_result(scan_result)

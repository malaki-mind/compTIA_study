# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:25:51 2026

@author: 19735
"""
import random

name = 0
number = 1

ports = { "FTP": {"name" : "File Transfer Protocol (FTP)", 
                  "number": "20/21"},
         "SSH" : {"name" : "Secure Shell (SSH)", 
                  "number" : "22"},
         "Telnet" : {"name" : "Telnet", 
                     "number" : "23"},
         "SMTP" : {"name" : "Simple Mail Transfer Protocol (SMTP)",
                   "number" : "25"},
         "DNS" : {"name" : "Domain Name System (DNS)",
                  "number" : "53"},
         "DHCP" : {"name" : "Dynamic Host Configuration Protocol (DHCP)",
                   "number" : "67/68"},
         "HTTP" : {"name" : "HyperText Transfer Protocol (HTTP)",
                   "number" : "80"},
         "POP3" : {"name" : "Post Office Protocol v3 (POP3)",
                   "number" : "110"},
         "NetBIOS/NetBT" : {"name" : "NetBIOS, NetBT",
                          "number" : "137, 138, 139"}
         
         }

port_list = []

for item in ports:
    print(ports[item].values())
    port_list.append(list(ports[item].values()))
    print (port_list)
    
random.shuffle(port_list)

for port in port_list:
    print(port[number])


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
                          "number" : "137, 138, 139"},
         "IMAP" : {"name" : "Internet Mail Access Protocol (IMAP)",
                   "number" : "153"},
         "SNMP" : {"name" : "Simple Network Management Protocol (SNMP)",
                   "number" : "161/162"},
         "LDAP" : {"name" : "Lightweight Directory Access Protocol (LDAP)",
                   "number" : "389"},
         "HTTPS" : {"name" : "HyperText Transfer Protocol Secure (HTTPS)",
                    "number" : "443"},
         "SMB/CIFS" : {"name" : "Server Message Block (SMB)/Common Internet File System (CIFS)",
                       "number" : "445"},
         "RDP" : {"name" : "Remote Desktop Protocol",
                  "number" : "3389"}
         
         }

## make function to take dict and make into a list, then randomize
def dict_to_list(dictionary):
    new_list = []

    for item in dictionary:
        new_list.append(list(dictionary[item].values()))    
    
    return new_list

def print_list(new_list):
    for i in new_list:
        print(i)
     
def print_port(port_dict, protocol):
    p_data = port_dict[protocol]
    try:
        p_data
    except:
        print("Protocol not found")
    else:
        print(p_data.get("name"), "is in Port", p_data.get("number"))
        
## create practice drill functions, IE loop til correct, no scores taken
## one for guessing port numbers

port_list = dict_to_list(ports)

def drill(dictionary, question, key_1, key_2):
    new_list = dict_to_list(dictionary)
    random.shuffle(new_list)
    user_input = ""
    for item in new_list:
        user_input = str(input(f"{item[key_1]} {question}\n"))
        while(user_input != item[key_2]):
            user_input = str(input(f"wrong\n"))
        print("correct!")
        

## one for guessing port names
## one for guessing Wifi frequency
## one for guessing Wifi transfer data rate
## one for guessing Wifi ranges
        
## create quiz with scores given, only one shot to answer each question
## create menu to choose btwn these options
drill(ports, "is in which port?", name, number)
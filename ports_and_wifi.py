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
         "RDP" : {"name" : "Remote Desktop Protocol (RDP)",
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

def drill(dictionary, question, q, a):
    new_list = dict_to_list(dictionary)
    random.shuffle(new_list)
    user_input = ""
    for item in new_list:
        user_input = str(input(f"{item[q]} {question}\n"))
        while(user_input != item[a]):
            user_input = str(input(f"wrong\n"))
        print("correct!")

def quiz(dictionary, question, q, a):    
    new_list = dict_to_list(dictionary)
    score = 0
    ceiling = len(new_list)
    random.shuffle(new_list)
    user_input = ""
    for item in new_list:
        user_input = str(input(f"{item[q]} {question}\n"))
        if (user_input == item[a]):
            score += 1
        else:
            print("wrong")
    return score/ceiling * 100

def menu():
    user_input = 100
    upper_limit = 6
    lower_limit = 1
    print("CompTIA Ports, Protocols, and Wifi")
    print(f"1. Find Port by Protocol\n2. Port Number Drill")
    print(f"3. Protocol Drill\n4. Port Number Quiz\n5. Protocol Quiz")
    print("6. Quit")
   
    while ((user_input > upper_limit) or (user_input < lower_limit)):
        user_input = int(input("Choose an option: "))
        if ((user_input > upper_limit) or (user_input < lower_limit)):
            print("invalid response")
    return user_input
     
## one for guessing port names
## one for guessing Wifi frequency
## one for guessing Wifi transfer data rate
## one for guessing Wifi ranges
        
## create quiz with scores given, only one shot to answer each question
## create menu to choose btwn these options

class Menu_Options:
    PORT_FIND = 1
    PORT_NUM_DRILL = 2
    PORT_PRO_DRILL = 3
    PORT_NUM_QUIZ = 4
    PORT_PRO_QUIZ = 5
    QUIT = 6

def main():

    menu_choice = -1
    while(menu_choice != Menu_Options.QUIT):
        menu_choice = menu()
        match menu_choice:
            case Menu_Options.PORT_FIND:
                user_input = str(input("Enter a Protocol Abbreviation: "))
                print_port(ports, user_input)
            case Menu_Options.PORT_NUM_DRILL:
                drill(ports, "is in which port?", name, number)
            case Menu_Options.PORT_PRO_DRILL:
                drill(ports, "has which protocol?", number, name)
            case Menu_Options.PORT_NUM_QUIZ:
                print(quiz(ports, "is in which port?", name, number))
            case Menu_Options.PORT_PRO_QUIZ:
                print(quiz(ports, "has which protocol?", number, name))
            case _:
               print("how?")

#total_score = quiz(ports, "is in which port?", name, number)
#print(total_score)
main()
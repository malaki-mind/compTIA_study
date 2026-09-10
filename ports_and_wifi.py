# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:25:51 2026

@author: 19735
"""
import random
## make CONST CLASSES for index values and dictionaries

class Ports_Index:
    # port indices
    NAME = 0
    NUMBER = 1
class Wifi_Index:
    STANDARD = 0
    FREQ = 1
    SPEED = 2
    RANGE = 3
    
class Port_Dict:
    PORTS = { "FTP": {"name" : "File Transfer Protocol (FTP)", 
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
class Wifi_Dict:
    WIFI = { "Wifi 1" : {"standard" : "802.11b (Wifi 1)",
                          "frequency" : "2.4 GHz",
                          "speed" : "11 Mbps",
                          "range" : "35m (indoor)/140m (outdoor)"},
            "Wifi 2" : {"standard" : "802.11a (Wifi 2)",
                         "frequency" : "5 GHz",
                         "speed" : "54 Mbps",
                         "range" : "35m (indoor)/120m (outdoor)"},
            "Wifi 3" : {"standard" : "802.11g (Wifi 3)",
                         "frequency" : "2.4 GHz",
                         "speed" : "54 Mbps",
                         "range" : "38m (indoor)/140m (outdoor)"},
            "Wifi 4" : {"standard" : "802.11n (Wifi 4)",
                         "frequency" : "2.4 / 5 GHz",
                         "speed" : "600 Mbps",
                         "range" : "70m (indoor)/250m (outdoor)"},
            "Wifi 5" : {"standard" : "802.11ac (Wifi 5)",
                         "frequency" : "5 GHz",
                         "speed" : "1 - 6.9 Gbps",
                         "range" : "35m (indoor)"},
            "Wifi 6" : {"standard" : "802.11ax (Wifi 6)",
                         "frequency" : "2.4 / 5 GHz",
                         "speed" : "9.6 Gbps",
                         "range" : "30m (indoor)/120m (outdoor)"},
            "Wifi 6e" : {"standard" : "802.11ax (Wifi 6e)",
                         "frequency" : "2.4 / 5 / 6 GHz",
                         "speed" : "9.6 Gbps",
                         "range" : "30m (indoor)/120m (outdoor)"},
            "Wifi 7" : {"standard" : "802.11be (Wifi 7)",
                         "frequency" : "2.4 / 5 / 6 GHz",
                         "speed" : "30 - 40 Gbps",
                         "range" : "30m (indoor)/120m (outdoor)"},
            }
        
    
class Menu_Options:
    PORT_FIND = 1
    PORT_NUM_DRILL = 2
    PORT_PRO_DRILL = 3
    PORT_NUM_QUIZ = 4
    PORT_PRO_QUIZ = 5
    WIFI_FIND = 6
    WIFI_FREQ_DRILL = 7
    WIFI_SPEED_DRILL = 8
    WIFI_RANGE_DRILL = 9
    WIFI_FREQ_QUIZ = 10
    WIFI_SPEED_QUIZ = 11
    WIFI_RANGE_QUIZ = 12
    QUIT = 13

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

def print_wifi(wifi_dict, generation):
    w_data = wifi_dict[generation]
    try:
        w_data
    except:
        print("Wifi Generation not found")
    else:
        print(w_data)
        
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
    upper_limit = Menu_Options.QUIT
    lower_limit = 1
    print("CompTIA Ports, Protocols, and Wifi")
    print(f"1. Find Port by Protocol\n2. Port Number Drill")
    print(f"3. Protocol Drill\n4. Port Number Quiz\n5. Protocol Quiz")
    print(f"6. Wifi Info by Gen\n7. Wifi Frequency Drill\n8. Wifi Speed Drill")
    print(f"9. Wifi Range Drill\n10. Wifi Frequency Test\n11. Wifi Speed Quiz")
    print(f"12. Wifi Range Quiz\n13. Quit")

    while ((user_input > upper_limit) or (user_input < lower_limit)):
        try:
            user_input = int(input("Choose an option: "))
        except:
            print("nice")
        else:
            if ((user_input > upper_limit) or (user_input < lower_limit)):
                print("invalid response")
    return user_input

def main():
    menu_choice = -1
    while(menu_choice != Menu_Options.QUIT):
        menu_choice = menu()
        match menu_choice:
            ## Port Options
            case Menu_Options.PORT_FIND:
                user_input = str(input("Enter a Protocol Abbreviation: "))
                print_port(Port_Dict.PORTS, user_input)
            case Menu_Options.PORT_NUM_DRILL:
                drill(Port_Dict.PORTS, "is in which port?", 
                      Ports_Index.NAME, Ports_Index.NUMBER)
            case Menu_Options.PORT_PRO_DRILL:
                drill(Port_Dict.PORTS, "has which protocol?", 
                      Ports_Index.NUMBER, Ports_Index.NAME)
            case Menu_Options.PORT_NUM_QUIZ:
                print(quiz(Port_Dict.PORTS, "is in which port?", 
                           Ports_Index.NAME, Ports_Index.NUMBER))
            case Menu_Options.PORT_PRO_QUIZ:
                print(quiz(Port_Dict.PORTS, "has which protocol?", 
                           Ports_Index.NUMBER, Ports_Index.NAME))
            ## Wifi Options
            case Menu_Options.WIFI_FIND:
                user_input = str(input("Enter Wifi Generation: "))
                print_wifi(Wifi_Dict.WIFI, user_input)
            case Menu_Options.WIFI_FREQ_DRILL:
                drill(Wifi_Dict.WIFI, "is on what frequency?",
                      Wifi_Index.STANDARD, Wifi_Index.FREQ)
            case Menu_Options.WIFI_SPEED_DRILL:
                drill(Wifi_Dict.WIFI, "operates at what max data rate?",
                      Wifi_Index.STANDARD, Wifi_Index.SPEED)
            case Menu_Options.WIFI_RANGE_DRILL:
                drill(Wifi_Dict.WIFI, "spans what maximum distance?",
                      Wifi_Index.STANDARD, Wifi_Index.RANGE)
            case Menu_Options.WIFI_FREQ_QUIZ:
                print(quiz(Wifi_Dict.WIFI, "is on what frequency?",
                      Wifi_Index.STANDARD, Wifi_Index.FREQ))
            case Menu_Options.WIFI_SPEED_QUIZ:
                print(quiz(Wifi_Dict.WIFI, "operates at what max data rate?",
                      Wifi_Index.STANDARD, Wifi_Index.SPEED))
            case Menu_Options.WIFI_RANGE_QUIZ:
                print(quiz(Wifi_Dict.WIFI, "spans what maximum distance?",
                      Wifi_Index.STANDARD, Wifi_Index.RANGE))
            case _:
               break
class Func:
            
    test = { Menu_Options.PORT_FIND : print_port}
    
class Para:
    test = {"dict" : Port_Dict.PORTS,
            "para" : "FTP"}
    
Func.test[Menu_Options.PORT_FIND](Para.test.get("dict"), Para.test.get("para"))

#main()
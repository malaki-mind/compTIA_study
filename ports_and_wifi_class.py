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
    
class Option:
    def __init__(self, menu = 0, funct = 1, ):
        self.menu = menu
        self.funct = funct
        self.choice_dict = {self.menu : None,
                            self.funct : None}
        self.menu_opts = self.choice_dict[self.menu]
        self.funct_opts = self.choice_dict[self.funct]
        #self.menu_choices = self.menu_opts.keys()
        
        
    def print_menu(self):
        for key in self.menu_opts:
            print(f"{key}. {self.menu_opts[key]}")
    
    def inp(self):
        user_input = str(input("Choose Option: "))
        return user_input
    
    def choose(self, user_input):
        self.menu_opts[user_input]
        self.funct_opts[user_input]()
    
class Study_Option(Option):
    def __init__(self, opt_num = "0"):
        self.opt_num = opt_num
        self.find = "1"
        self.drill = "2"
        self.quiz = "3"
        self.study_opts = {self.find : "Find",
                           self.drill : "Drills",
                           self.quiz : "Quizzes"}
        self.menu_opts = {self.find : None,
                          self.drill : None,
                          self.quiz : None}
        self.funct_opts = {self.find : None,
                           self.drill : None,
                           self.quiz : None}
        self.templates = {self.find : None,
                          self.drill : None,
                          self.quiz : None}
        self.study_data = None
        
    def dict_to_list(self):
        new_list = []        
        try:        
            for item in self.study_data:
                new_list.append(list(self.study_data[item].values()))        
        except:
            print("error")
        return new_list
            
    def find_funct(self, prompt):
        query = str(input(prompt))
        answer = self.study_data[query]
        try:
            answer
        except:
            print("Not found")
        else:
            print(self.study_data[query])
            
    def study_menu(self):
        for key in self.study_opts:
            print(f"{key}. {self.study_opts[key]}")
        
    def study_choose(self):
        self.study_menu()
        menu_choice = self.inp()
        if menu_choice in (self.find, self.drill, self.quiz):
            for opts in self.menu_opts[menu_choice]:
                print(f"{opts}. {self.menu_opts[menu_choice][opts]}")
            funct_choice = self.inp()
        else:
            funct_choice = "q"
        return [menu_choice, funct_choice]
        
    def activate(self, menu_choice, *args, **kwargs):
        if menu_choice == self.find:
            self.funct_opts[menu_choice](args[0])
        else:
            self.funct_opts[menu_choice](**kwargs)
        
    def drill_funct(self, question, q, a):
        new_list = self.dict_to_list()
        random.shuffle(new_list)
        user_input = ""
        for item in new_list:
            user_input = str(input(f"{item[q]} {question}\n"))
            while(user_input != item[a]):
                user_input = str(input(f"wrong\n"))
            print("correct!")
    
    def quiz_funct(self, question, q, a):    
        new_list = self.dict_to_list()
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
        return print("Score: ", score/ceiling * 100)
    
    def test_choice(self):
            user_choices = self.study_choose()
            if user_choices[0] in (self.find, self.drill, self.quiz):
                menu_choice = user_choices[0]
                funct_choice = user_choices[1]
            #print(ports.templates[menu_choice][funct_choice])
                if funct_choice in (self.find, self.drill, self.quiz):
                    match menu_choice:
                        case self.find:
                            self.activate(menu_choice, self.templates[menu_choice][funct_choice])
                        case _:
                            self.activate(menu_choice, **self.templates[menu_choice][funct_choice])
                    
class study:
    PORTS_BY_NUM = "1"
    PORTS_BY_NAME = "2"
    WIFI_FREQ = "1"
    WIFI_SPEED = "2"
    WIFI_RANGE = "3"

def main():
    user_inp = ""
    main_menu = Option()
    ports = Study_Option("1")
    wifi = Study_Option("2")

    main_menu.menu_opts = {ports.opt_num : "Ports",
                           wifi.opt_num : "Wifi"}
    main_menu.funct_opts = {ports.opt_num : ports.study_menu,
                            wifi.opt_num : wifi.study_menu}
    
    ports.templates[ports.find] = ({"1" : "Enter Protocol Abbreviation: "})
    ports.templates[ports.drill] = { study.PORTS_BY_NUM : 
                                        {"question" : "is in which port?", 
                                         "q" : Ports_Index.NAME,
                                         "a" : Ports_Index.NUMBER 
                                         },
                                    study.PORTS_BY_NAME : 
                                        {"question" : "has which protocol?",
                                        "q" : Ports_Index.NUMBER,
                                        "a" : Ports_Index.NAME
                                        }
                                    }
    ports.templates[ports.quiz] = ports.templates[ports.drill]
    ports.menu_opts[ports.find] = {"1" : "Find by Protocol"}
    ports.menu_opts[ports.drill] = {study.PORTS_BY_NUM : "Port Number Drill",
                                    study.PORTS_BY_NAME: "Protocols Drill"}
    ports.menu_opts[ports.quiz] = {study.PORTS_BY_NUM : "Port Number Quiz",
                                   study.PORTS_BY_NAME : "Protocols Quiz"}
    ports.funct_opts[ports.find] = ports.find_funct
    ports.funct_opts[ports.drill] = ports.drill_funct
    ports.funct_opts[ports.quiz] = ports.quiz_funct
    wifi.templates[wifi.find] = ({"1" : "Enter Wifi Generation: "})
    wifi.templates[wifi.drill] = {study.WIFI_FREQ :
                                  {"question" : "is on what frequency?",
                                   "q" : Wifi_Index.STANDARD,
                                   "a" : Wifi_Index.FREQ
                                   },study.WIFI_SPEED :
                                  {"question" : "operates at what max data rate?",
                                   "q" : Wifi_Index.STANDARD,
                                   "a" : Wifi_Index.SPEED
                                  },study.WIFI_RANGE : 
                                   {"question" : "spans what maximum distance?",
                                    "q" : Wifi_Index.STANDARD,
                                    "a" : Wifi_Index.RANGE
                                   }
                                 }
    wifi.templates[wifi.quiz] = wifi.templates[wifi.drill]

    wifi.menu_opts[wifi.find] = {"1" : "Find by Generation"}
    wifi.menu_opts[wifi.drill] = {study.WIFI_FREQ : "Wifi Frequency Drill",
                                  study.WIFI_SPEED : "Wifi Data Rate Drill",
                                  study.WIFI_RANGE : "Wifi Range Drill"}
    wifi.menu_opts[wifi.quiz] = {study.WIFI_FREQ : "Wifi Frequency Quiz",
                                  study.WIFI_SPEED : "Wifi Data Rate Quiz",
                                  study.WIFI_RANGE : "Wifi Range Quiz"}

    wifi.funct_opts[wifi.find] = wifi.find_funct
    wifi.funct_opts[wifi.drill] = wifi.drill_funct
    wifi.funct_opts[wifi.quiz] = wifi.quiz_funct
    
    ports.study_data = Port_Dict.PORTS
    wifi.study_data = Wifi_Dict.WIFI
 
    
    while (user_inp != "q"):
        main_menu.print_menu()
        user_inp = main_menu.inp()


        match user_inp:
            case ports.opt_num:
                ports.test_choice()
            case wifi.opt_num:
                wifi.test_choice()
            
            
main()
    


    
    
    

"""
main_menu = Option()
main_menu.menu_opts = {ports.opt_num : "Ports",
                           wifi.opt_num : "Wifi"}
main_menu.funct_opts = {ports.opt_num : ports.study_menu,
                            wifi.opt_num : wifi.study_menu}
"""
"""
ports.templates[ports.find] = ({"1" : "Enter Protocol Abbreviation: "})
ports.templates[ports.drill] = { study.PORTS_BY_NUM : 
                                    {"question" : "is in which port?", 
                                     "q" : Ports_Index.NAME,
                                     "a" : Ports_Index.NUMBER 
                                     },
                                study.PORTS_BY_NAME : 
                                    {"question" : "has which protocol?",
                                    "q" : Ports_Index.NUMBER,
                                    "a" : Ports_Index.NAME
                                    }
                                }
ports.templates[ports.quiz] = ports.templates[ports.drill]
"""
"""
ports.menu_opts[ports.find] = {"1" : "Find by Protocol"}
ports.funct_opts[ports.find] = ports.find_funct

ports.menu_opts[ports.drill] = {study.PORTS_BY_NUM : "Port Number Drill",
                                study.PORTS_BY_NAME: "Protocols Drill"}
ports.funct_opts[ports.drill] = ports.drill_funct

ports.menu_opts[ports.quiz] = {study.PORTS_BY_NUM : "Port Number Quiz",
                               study.PORTS_BY_NAME : "Protocols Quiz"}
ports.funct_opts[ports.quiz] = ports.quiz_funct

wifi.templates[wifi.find] = ({"1" : "Enter Wifi Generation: "})
wifi.templates[wifi.drill] = {study.WIFI_FREQ :
                              {"question" : "is on what frequency?",
                               "q" : Wifi_Index.STANDARD,
                               "a" : Wifi_Index.FREQ
                               },study.WIFI_SPEED :
                              {"question" : "operates at what max data rate?",
                               "q" : Wifi_Index.STANDARD,
                               "a" : Wifi_Index.SPEED
                              },study.WIFI_RANGE : 
                               {"question" : "spans what maximum distance?",
                                "q" : Wifi_Index.STANDARD,
                                "a" : Wifi_Index.RANGE
                               }
                             }
wifi.templates[wifi.quiz] = wifi.templates[wifi.drill]

wifi.menu_opts[wifi.find] = {"1" : "Find by Generation"}
wifi.menu_opts[wifi.drill] = {study.WIFI_FREQ : "Wifi Frequency Drill",
                              study.WIFI_SPEED : "Wifi Data Rate Drill",
                              study.WIFI_RANGE : "Wifi Range Drill"}
wifi.menu_opts[wifi.quiz] = {study.WIFI_FREQ : "Wifi Frequency Quiz",
                              study.WIFI_SPEED : "Wifi Data Rate Quiz",
                              study.WIFI_RANGE : "Wifi Range Quiz"}

wifi.funct_opts[wifi.find] = wifi.find_funct
wifi.funct_opts[wifi.drill] = wifi.drill_funct
wifi.funct_opts[wifi.quiz] = wifi.quiz_funct

ports.study_data = Port_Dict.PORTS
wifi.study_data = Wifi_Dict.WIFI
"""



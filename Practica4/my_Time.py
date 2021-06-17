import time 
from threading import Thread
from tkinter import *

import socket
import sys


#00:00:00

Horas=[]
HoraGlobal=[]
Direcciones=[]

class my_clk:
    cur_time = time.strftime("%H:%M:%S")
    parts = cur_time.split(':')
    hora = int(parts[0])
    minuto = int(parts[1])
    segundo = int(parts[2])
    vel = 1

    def let_my_time(self):
        while True:
            self.segundo+=1
            if(self.segundo>=60):
                self.segundo=0
                self.minuto+=1
            if(self.minuto>=60):
                self.minuto=0
                self.hora+=1
            if(self.hora>=24):
                self.hora=0
            time.sleep(1/self.vel)
            #self.get_time()
    
    def prueba(self):
        self.let_my_time(1)

    
    def get_time(self):
        return "{:02}:{:02}:{:02}".format(self.hora,self.minuto,self.segundo)

def obtenerHoraLocal():
    horaUTC = time.strftime("%H:%M:%S")
    Horas.append(horaUTC)

def modificarHora(data):
    
    cur_time = data.decode()
    parts = cur_time.split(':')
    hora = int(parts[0])
    minuto = int(parts[1])
    segundo = int(parts[2])
    

def agregarDireccion(direccion):
    if(len(Direcciones)==0):
        Direcciones.append(direccion)
        #print('Direcciones'+ str(len(Direcciones)))
        i=0
    i=0
    while(i<len(Direcciones)):
        if(direccion!=Direcciones[i]):
            Direcciones.append(direccion)
            #print('Direcciones'+str(len(Direcciones)))
            #print(direccion)
        i=i+1

def calcularHoraGlobal(Horas,address):

    if(len(Horas)==3):
        seconds = 0
        minuts = 0
        obtenerHoraLocal()
        i=0
        minutos=0
        #print(Horas)
        while(i<len(Horas)):
            cur_time = Horas[i]
            #print(cur_time)
            parts = cur_time.split(':')
            #print("Viene del my time")
            #print(parts)
            hora = int(parts[0])
            minuto = int(parts[1])
            segundo = int(parts[2])
            seconds+=minuto*60+hora*60*60+segundo
            minuts += hora*60+minuto+segundo/60
            #print(Horas[i])
            i=i+1
            #print(minutos)
        promedio=seconds/len(Horas)
        hours = seconds%3600
        #print(promedio)
        aux='{:02}:{:02}:{:02}'.format(int(promedio/3600), int((minuts/4))%60, int((seconds/4)%60))
        #print('La hora establecida es: '+ aux)
        Horas.clear()
        return aux


def iniciar():
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    my_aux = ""

    while True:
        #print('\nEsperando del servidor tiempo')
        data, address = sock.recvfrom(4096)
        #print("Address: ", address)
        if(data.decode()==''):
            cur_time = time.strftime("%H:%M:%S")
            #template = "La hora local es: " + time
            #print(template)
            #print("No llego hora al servidor Tiempo")
        else:
            #print(data.decode())
            minuto=data.decode()
            Horas.append(str(minuto))
            #print(minuto)
            agregarDireccion(address)
            my_aux = calcularHoraGlobal(Horas,address)
            if my_aux != None:
                sock.sendto(my_aux.encode(), address)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s = Thread(target=iniciar)
s.daemon = True
s.start()

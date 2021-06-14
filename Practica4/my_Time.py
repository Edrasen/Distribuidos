import time 
from threading import Thread
from tkinter import *

#00:00:00

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

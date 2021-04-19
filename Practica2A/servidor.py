import rpyc 
import time
from rpyc.utils.server import ThreadedServer
from tkinter import *
from threading import Thread


        #return "{:02}:{:02}:{:02}".format(self.hora,self.minuto,self.segundo)

class RPC_Clock(rpyc.Service):

    def __init__(self):
        self.cur_time = time.strftime("%H:%M:%S")
        self.parts  = self.cur_time.split(':')
        self.hora = int(self.parts[0])
        self.minuto = int(self.parts[1])
        self.segundo = int(self.parts[2])
        self.vel = 1

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
            
    
    def exposed_prueba(self):
        print("New clock")
        clk = Thread(target=self.let_my_time)
        clk.start()

    def exposed_get_time(self):
        return "{:02}:{:02}:{:02}".format(self.hora,self.minuto,self.segundo)

    def exposed_set_time(self):
        self.modificar = Tk()
        self.modificar.title("modificar reloj")
        self.lblh = Label(self.modificar, text="Hora: ")
        self.lblh.grid(column=0,row=0)
        self.in_h = Entry(self.modificar,width=15)
        self.in_h.grid(column=1,row=0)
        self.lblm = Label(self.modificar, text="Minuto: ")
        self.lblm.grid(column=0,row=1)
        self.in_m = Entry(self.modificar,width=15)
        self.in_m.grid(column=1,row=1)
        self.lbls = Label(self.modificar, text="Segundo: ")
        self.lbls.grid(column=0,row=2)
        self.in_s = Entry(self.modificar,width=15)
        self.in_s.grid(column=1,row=2)

        self.lblv = Label(self.modificar, text="Velocidad: ")
        self.lblv.grid(column=0,row=3)
        self.in_v = Entry(self.modificar,width=15)
        self.in_v.grid(column=1,row=3)

        self.ac = Button(self.modificar,text="Aceptar", command=lambda : self.accept(int(self.in_v.get())))
        self.ac.grid(column=1,row=5)
        self.modificar.mainloop()
        
        
    def accept(self,vel):
        self.hora = int(self.in_h.get())%24
        self.minuto = int(self.in_m.get())%60
        self.segundo = int(self.in_s.get())%60
        self.vel = int(vel)
        self.modificar.destroy()
        print("New clock started")
        clk = Thread(target=self.let_my_time)
        clk.start()
        return

if __name__ == "__main__":
    server = ThreadedServer(RPC_Clock, port=12345)
    print("Server started...")
    server.start()

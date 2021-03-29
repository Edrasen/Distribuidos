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

    def let_my_time(self,vel):
        while True:
            self.segundo+=1
            if(self.segundo==60):
                self.segundo=0
                self.minuto+=1
            if(self.minuto==60):
                self.selminuto=0
                self.hora+=1
            if(self.hora==24):
                self.hora=0
            time.sleep(1/vel)
            self.get_time()
    
    def prueba(self):
        self.let_my_time(1)

    
    def get_time(self):
        return "{:02}:{:02}:{:02}".format(self.hora,self.minuto,self.segundo)

    def set_time(self):
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
        # self.hora = int((input("Hora: ")))
        # self.minuto = int(input("Minuto: "))
        # self.segundo = int(input("Segundo: "))
        # self.let_my_time()
        
    def accept(self,vel):
        self.hora = int(self.in_h.get())
        self.minuto = int(self.in_m.get())
        self.segundo = int(self.in_s.get())
        self.modificar.destroy()
        self.let_my_time(vel)
        return 


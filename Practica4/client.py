import rpyc
import time
from tkinter import *
from threading import Thread

c = rpyc.connect('localhost',12345)


root=Tk()
root.title("MY CLOCK")
root.configure(bg="white")
datos = Label(root,width=40, height=10)


def pedir_libro():
    datosLibro = c.root.book1()
    print(datosLibro)
    if not datosLibro:
            datos.config(text="NO hay más libros", bg="white",fg="red",font="Verdana 12")
            buttonP["state"] = DISABLED
    else:
        datos.config(text=datosLibro,bg="white",fg="black",font="Verdana 12")


def reset():
    c.root.reset()
    datos.config(text="Sesión reiniciada\nTODOS LOS LIBROS ESTAN DISPONIBLES", bg="white",fg="blue",font="Verdana 12")

buttonP = Button(root,text="Pedir libro",command=pedir_libro)
buttonR = Button(root,text="Reiniciar sesión",command=reset)

class Reloj:
    flag = 1
    hard_flag = 1
    def get_time(self):
        self.my_new_t, self.hard_flag = c.root.time1()
        #print(self.hard_flag)        
        if not self.hard_flag:
            datos.config(text="REINICIO DESDE SERVIDOR", bg="white",fg="red",font="Verdana 12") 
            self.hard_flag = 1
            self.clock.config(text=self.my_new_t,bg="white",fg="red",font="Verdana 25")
            if self.flag:
                self.clock.after(100,self.get_time)        
            else:
                self.flag = 1
        else:
            self.clock.config(text=self.my_new_t,bg="white",fg="red",font="Verdana 25")
            if self.flag:
                self.clock.after(100,self.get_time)        
            else:
                self.flag = 1



    def init_clock(self):
        self.current_time=""
        self.clock = Label(root)    
        self.clock.grid(row=2,column=2,pady=25,padx=25)
        datos.grid(row=2,column=3,pady=5,padx=5)
        buttonP.grid(row=3,column=3,pady=2,padx=2)
        buttonR.grid(row=4,column=3,pady=2,padx=2)
        self.get_time()
    



myclk = Reloj()
myclk.init_clock()

root.mainloop()
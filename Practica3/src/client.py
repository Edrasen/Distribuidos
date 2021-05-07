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
    datos.config(text=datosLibro,bg="white",fg="black",font="Verdana 12")
    if datosLibro == None:
        datos.config(text="NO hay más libros", bg="white",fg="red",font="Verdana 20")
        buttonP["state"] = DISABLED

buttonP = Button(root,text="Pedir libro",command=pedir_libro)

class Reloj:
    flag = 1
    def get_time(self):
        self.my_new_t = c.root.time1()        
        self.clock.config(text=self.my_new_t,bg="white",fg="red",font="Verdana 50")
        if self.flag:
            self.clock.after(100,self.get_time)        
        else:
            self.flag = 1



    def init_clock(self):
        self.current_time=""
        self.clock = Label(root)    
        self.clock.grid(row=2,column=2,pady=25,padx=25)
        datos.grid(row=2,column=3,pady=5,padx=5)
        buttonP.grid(row=3,column=3,pady=5,padx=5)
        self.get_time()
    



myclk = Reloj()
myclk.init_clock()

root.mainloop()
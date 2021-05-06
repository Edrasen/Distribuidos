import rpyc
import time
from tkinter import *
from threading import Thread

c = rpyc.connect('localhost',12345)


root=Tk()
root.title("MY CLOCK")
root.configure(bg="white")

class Reloj:
    flag = 1
    def get_time(self):
        # print(c.root.get_time())
        # time.sleep(1)
        # get_time()
        self.my_new_t = c.root.time2()        
        self.clock.config(text=self.my_new_t,bg="white",fg="red",font="Verdana 50")
        if self.flag:
            self.clock.after(100,self.get_time)        
        else:
            self.flag = 1
            #self.stop2()


    def init_clock(self):
        #c.root.prueba()
        self.current_time=""
        self.clock = Label(root)    
        self.clock.grid(row=2,column=2,pady=25,padx=25)
        self.get_time()
    


myclk = Reloj()
myclk.init_clock()

root.mainloop()
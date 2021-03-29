from  tkinter import *
import time
from threading import Thread
from my_Time import my_clk

root=Tk()
root.title("MULTIPLE CLOCKS")
root.configure(bg="white")
t_clocks = []
clks = []

class reloj: 
    flag = 1
    def init_clock(self,r,c):
        self.current_time=""
        self.clock = Label(root)    
        self.clock.grid(row=r+2,column=c,pady=25,padx=25)
        self.times()
        #self.new_time()

    def times(self):
        self.current_time=time.strftime("%H:%M:%S")
        self.clock.config(text=self.current_time,bg="white",fg="blue",font="Verdana 50")
        if self.flag:
            self.clock.after(200,self.times)
        else:
            self.flag = 1
            self.stop()

    def stop(self):       
        self.current_time=time.strftime("%H:%M:%S")
        self.clock.config(text=self.current_time,bg="white",fg="red",font="Verdana 50")
        self.new_time()

    def new_time(self):
        self.my_clock = my_clk()
        t_new_c = Thread(target=self.my_clock.set_time)
        t_new_c.daemon = True
        t_new_c.start()
        self.init_new_clk()


    def stop2(self):       
        self.my_new_t = self.my_clock.get_time()
        self.clock.config(text=self.my_new_t,bg="white",fg="red",font="Verdana 50")
        self.new_time()


    def init_new_clk(self):
        self.my_new_t = self.my_clock.get_time()        
        self.clock.config(text=self.my_new_t,bg="white",fg="red",font="Verdana 50")
        if self.flag:
            self.clock.after(100,self.init_new_clk)        
        else:
            self.flag = 1
            self.stop2()
        
        
def change(opt):
    clks[opt-1].flag = 0
    

for r in range(0,2):
    for c in range(0,2):
        clk = reloj()
        clks.append(clk)
        t_clock = Thread(target=clk.init_clock,args=(r,c))
        t_clocks.append(t_clock)

for tclk in t_clocks:
    tclk.daemon = True
    tclk.start()




boton = Button(root,text="MODIFICAR 1",command=lambda: change(1))
boton.grid(row=1, column=0)
boton2 = Button(root,text="MODIFICAR 2",command=lambda: change(2))
boton2.grid(row=1, column=1)
boton3 = Button(root,text="MODIFICAR 3",command=lambda: change(3))
boton3.grid(row=4, column=0)
boton4 = Button(root,text="MODIFICAR 4",command=lambda: change(4))
boton4.grid(row=4, column=1)



root.mainloop()

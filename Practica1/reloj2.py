from  tkinter import *
import time
from threading import Thread

root=Tk()
root.title("MULTIPLE CLOCKS")
t_clocks = []

class reloj: 
    clock = NONE
    flag = 1
    def init_clock(self,r,c):
        self.current_time=""
        self.clock = Label(root)    
        self.clock.grid(row=r+2,column=c,pady=25,padx=25)
        self.times()

    def times(self):
        self.current_time=time.strftime("%H:%M:%S")
        self.clock.config(text=self.current_time,bg="black",fg="green",font="Arial 50 bold")
        if self.flag:
            self.clock.after(200,self.times)
        else:
            self.stop()

    def stop(self):       
        self.current_time=time.strftime("%H:%M:%S")
        self.clock.config(text=self.current_time,bg="black",fg="green",font="Arial 50 bold")


clks = []
for r in range(0,2):
    for c in range(0,2):
        clk = reloj()
        clks.append(clk)
        t_clock = Thread(target=clk.init_clock,args=(r,c))
        t_clocks.append(t_clock)

for tclk in t_clocks:
    tclk.daemon = True
    tclk.start()


def change(opt):
    clks[opt-1].flag = 0
    


boton = Button(root,text="MODIFICAR1",command=lambda: change(1))
boton.grid(row=0, column=0)
boton = Button(root,text="MODIFICAR2",command=lambda: change(2))
boton.grid(row=0, column=1)
boton = Button(root,text="MODIFICAR3",command=lambda: change(3))
boton.grid(row=4, column=0)
boton = Button(root,text="MODIFICAR4",command=lambda: change(4))
boton.grid(row=4, column=1)
root.mainloop()

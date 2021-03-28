from  tkinter import *
import time
from threading import Thread

root=Tk()
root.title("MULTIPLE CLOCKS")
t_clocks = []

class reloj: 
    def init_clock(self,r,c):
        self.current_time=""
        self.clock = Label(root)    
        self.clock.grid(row=r,column=c,pady=25,padx=25)
        self.times()

    def times(self):
        self.current_time=time.strftime("%H:%M:%S")
        self.clock.config(text=self.current_time,bg="black",fg="green",font="Arial 50 bold")
        self.clock.after(200,self.times)
    
    def change(self):
        self.current_time.replace(self.current_time,"22:13:23")
        self.clock.config(text="self.current_time",bg="black",fg="green",font="Arial 50 bold")



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


root.mainloop()

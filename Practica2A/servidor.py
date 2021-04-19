from  tkinter import *
import time
import rpyc
from threading import Thread
from my_Time import my_clk
from rpyc.utils.server import ThreadedServer


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
            #print(self.current_time)
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
        self.clock.config(text=self.my_new_t,bg="white",fg="blue",font="Verdana 50")
        if self.flag:
            self.clock.after(100,self.init_new_clk)        
        else:
            self.flag = 1
            self.stop2()
        
        
def change(opt):
    clks[opt-1].flag = 0
    print("Modifying clock {}".format(opt-1))
    

for r in range(0,2):
    for c in range(0,3):
        if r == 0 and (c == 0 or c == 2):
            pass
        else:
            clk = reloj()
            clks.append(clk)
            t_clock = Thread(target=clk.init_clock,args=(r,c))
            t_clocks.append(t_clock)

for tclk in t_clocks:
    tclk.daemon = True
    tclk.start()


class RPC_Clock(rpyc.Service):
    def exposed_time1(self):
        return clks[1].my_new_t
    def exposed_time2(self):
        return clks[2].my_new_t
    def exposed_time3(self):
        return clks[3].my_new_t
    # def exposed_time(self):
    #     return clks[0].my_new_t    



boton = Button(root,text="MODIFICAR MASTER",command=lambda: change(1))
boton.grid(row=1, column=1)
boton3 = Button(root,text="MODIFICAR 1",command=lambda: change(2))
boton3.grid(row=4, column=0)
boton4 = Button(root,text="MODIFICAR 2",command=lambda: change(3))
boton4.grid(row=4, column=1)
boton4 = Button(root,text="MODIFICAR 3",command=lambda: change(4))
boton4.grid(row=4, column=2)


if __name__ == "__main__":
    server = ThreadedServer(RPC_Clock, port=12345)
    print("Server started...")
    s = Thread(target=server.start)
    s.daemon = True
    s.start()
    root.mainloop()

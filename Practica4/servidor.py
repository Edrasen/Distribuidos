from  tkinter import *
import time
import rpyc
from threading import Thread
from my_Time import my_clk
from rpyc.utils.server import ThreadedServer
import despachador as despach
import urllib.request
from PIL import Image, ImageTk
import io
import socket


root=Tk()
root.title("MULTIPLE CLOCKS")
root.configure(bg="white")
#root.geometry("800x420")
t_clocks = []
clks = []
hard_flag = 1


class reloj: 
    flag = 1
    def init_clock(self,r,c):
        self.my_clock = my_clk()
        self.t_new_c = Thread(target=self.my_clock.let_my_time)
        self.t_new_c.daemon = True
        self.t_new_c.start()
        self.current_time=""
        self.clock = Label(root)    
        self.clock.grid(row=r+2,column=c,pady=25,padx=25)
        self.times()
    #self.new_time()

    def times(self):
        self.current_time = self.my_clock.get_time()
        self.clock.config(text=self.current_time,bg="white",fg="blue",font="Verdana 20")
        if self.flag:
            self.clock.after(100,self.times)
            #print(self.current_time)
        else:
            self.flag = 1
            self.stop()

    def stop(self):       
        self.current_time2=time.strftime("%H:%M:%S")
        self.current_time=self.current_time2
        self.current_time = self.my_clock.get_time()
        self.clock.config(text=self.current_time,bg="white",fg="red",font="Verdana 20")
        self.t_new_c = Thread(target=self.set_time)
        self.t_new_c.daemon = True
        self.t_new_c.start()
        #self.set_time()
        #self.init_new_clk()
        

    def init_new_clk(self):
        self.current_time = self.my_clock.get_time()        
        self.clock.config(text=self.current_time,bg="white",fg="blue",font="Verdana 20")
        if self.flag:
            self.clock.after(100,self.init_new_clk)        
        else:
            self.flag = 1
            self.stop()


    def set_time(self):
        self.modificar = Toplevel(root)
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
    


        
    def accept(self,vel):
        self.my_clock.hora = int(self.in_h.get())%24
        self.my_clock.minuto = int(self.in_m.get())%60
        self.my_clock.segundo = int(self.in_s.get())%60
        self.my_clock.vel = vel
        self.modificar.destroy()
        print("Clock modified")
        self.init_new_clk()
        print(self.my_clock.hora)


    
    def stop2(self):       
        self.my_new_t = self.my_clock.get_time()
        self.clock.config(text=self.my_new_t,bg="white",fg="red",font="Verdana 20")
        self.new_time()
        self.times()

        
def change(opt):
    clks[opt-1].flag = 0
    print("Modifying clock {}".format(opt-1))

def ImgFromUrl(url):
    global image
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    im = im.resize((250, 350), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(im)
    return image


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

#despach.reset_status()

def modificarHora(data):
    
    print('Hora establecida {!r}'.format(data.decode()))

def EnviarHora():
    # Create a UDP socket
    global clks
    while True:
        server_address = ('localhost', 10000)
        #print(len(clks))
        for i in range(1,4):
            sent = sock.sendto(clks[i].current_time.encode(), server_address)      
        time.sleep(1)



def recv_time():
    while True:    
        try:
            data, server = sock.recvfrom(4096)
            new_time = data.decode()
            parts = new_time.split(':')
            #print("Mensaje recibido:"+ data.decode())

            clks[1].my_clock.hora = int(parts[0])
            clks[2].my_clock.hora = int(parts[0])
            clks[3].my_clock.hora = int(parts[0])

            clks[1].my_clock.minuto = int(parts[1])
            clks[2].my_clock.minuto = int(parts[1])
            clks[3].my_clock.minuto = int(parts[1])

            clks[1].my_clock.segundo = int(parts[2])
            clks[2].my_clock.segundo = int(parts[2])
            clks[3].my_clock.segundo = int(parts[2])

        except:
            print('No se pudo enviar')
        #time.sleep(4)

        

class RPC_Clock(rpyc.Service):
    global hard_flag
    def exposed_time1(self):
        return clks[1].current_time, hard_flag
    def exposed_time2(self):
        return clks[2].current_time, hard_flag
    def exposed_time3(self):
        return clks[3].current_time, hard_flag
    def exposed_book1(self):
        resp = despach.set_status("127.0.0.1:0402","Cliente1",clks[1].current_time)
        url = despach.portada   
        widget = Label(root, image=ImgFromUrl(url))
        widget.grid(row=2, column=5, pady=5, padx=5)
        return resp
    def exposed_book2(self):
        resp = despach.set_status("127.0.0.1:0202","Cliente2",clks[2].current_time)
        url = despach.portada   
        widget = Label(root, image=ImgFromUrl(url))
        widget.grid(row=2, column=5)
        return resp
    def exposed_book3(self):
        resp = despach.set_status("127.0.0.1:0106","Cliente3",clks[3].current_time)
        url = despach.portada   
        widget = Label(root, image=ImgFromUrl(url))
        widget.grid(row=2, column=5)
        return resp
    def exposed_reset(self):
        despach.reset_status()


def hard_Reset():
    global hard_flag
    hard_flag = 0
    despach.reset_status()
    time.sleep(2)
    hard_flag = 1



boton = Button(root,text="MODIFICAR MASTER",command=lambda: change(1))
boton.grid(row=1, column=1)
boton3 = Button(root,text="MODIFICAR 1",command=lambda: change(2))
boton3.grid(row=4, column=0)
boton4 = Button(root,text="MODIFICAR 2",command=lambda: change(3))
boton4.grid(row=4, column=1)
boton4 = Button(root,text="MODIFICAR 3",command=lambda: change(4))
boton4.grid(row=4, column=2)
botonR = Button(root,text="REINICIAR", command=hard_Reset)
botonR.grid(row=3, column=5)


if __name__ == "__main__":
    server = ThreadedServer(RPC_Clock, port=12345)
    print("Server started...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s = Thread(target=server.start)
    s.daemon = True
    s.start()

    e=Thread(target=EnviarHora)
    e.daemon=True
    e.start()

    r=Thread(target=recv_time)
    r.daemon=True
    r.start()

    root.mainloop()

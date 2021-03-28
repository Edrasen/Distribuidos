import time 
from threading import Thread

class my_clk:
    hora = 23
    minuto = 59
    segundo = 51

    def let_my_time(self):
        while True:
            self.segundo+=1
            if(self.segundo==60):
                self.segundo=0
                self.minuto+=1
            if(self.minuto==60):
                self.minuto=0
                self.hora+=1
            if(self.hora==24):
                self.hora=0
            time.sleep(1)
            self.get_time()
    
    def prueba(self):
        self.let_my_time()

    #print("{:02}:{:02}:{:02}".format(hora,minuto,segundo))
    def get_time(self):
        #print("{:02}:{:02}:{:02}".format(self.hora,self.minuto,self.segundo))
        return "{:02}:{:02}:{:02}".format(self.hora,self.minuto,self.segundo)

#myclock = my_clk()
#myclock.let_my_time()
#myclock.get_time()

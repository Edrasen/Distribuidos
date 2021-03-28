import time 
from threading import Thread

hora = 23
minuto = 59
segundo = 51

def let_my_time():
    global hora, segundo, minuto
    while True:
        segundo+=1
        if(segundo==60):
            segundo=0
            minuto+=1
        if(minuto==60):
            minuto=0
            hora+=1
        if(hora==24):
            hora=0
        time.sleep(1)
    #print("{:02}:{:02}:{:02}".format(hora,minuto,segundo))

def new_clk():
    Thread(target=let_my_time)

def get_time():
    return "{:02}:{:02}:{:02}".format(hora,minuto,segundo)

def prueba():
    new_clk()
import rpyc
import time
from tkinter import *
from threading import Thread

c = rpyc.connect('localhost',12345)
c.root.prueba()


def get_time():
    print(c.root.get_time())
    time.sleep(1)
    get_time()

get_time()
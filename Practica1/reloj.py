import sys
import time
from threading import Thread
from tkinter import *

root = Tk()
root.geometry("480x250")
root.title("Reloj digital con Tkinte")


def times():
    current_time = time.strftime("%H:%M:%S")
    return current_time

print(current_time+1)


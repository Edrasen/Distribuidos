from my_Time import my_clk
import time
from threading import Thread

my_clock = my_clk()

t_avr = Thread(target=my_clock.prueba)
t_avr.start()
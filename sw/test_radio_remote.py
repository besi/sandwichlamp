from machine import Pin
import time

b1 = Pin(34, Pin.IN)
b2 = Pin(33, Pin.IN)
b3 = Pin(39, Pin.IN)
b4 = Pin(36, Pin.IN)

while True:

    if b1.value():
        print("Button 1")
    if b2.value():
        print("Button 2")
    if b3.value():
        print("Button 3")
    if b4.value():
        print("Button 4")
    time.sleep(0.2)
    
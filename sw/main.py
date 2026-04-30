from machine import Pin
import asyncio
from primitives import ESP32Touch

touch1_pin = 14
touch2_pin = 32
touch3_pin = 4

ESP32Touch.threshold(80)
lamp = Pin(13, Pin.OUT)

mode = 1

def mode1():
    global mode
    mode = 1
    print("toggle lamp")
    lamp.value(1-lamp.value())
    
def mode2():
    global mode
    mode = 2
    import test_neopixel.py
    lamp.off()
    
def mode3():
    global mode
    mode = 3
    lamp.off()

async def main():
    t1 = ESP32Touch(Pin(touch1_pin), suppress=True)
    t1.press_func(lambda : mode1())
    t2 = ESP32Touch(Pin(touch2_pin), suppress=True)
    t2.press_func(lambda : mode2())
    t3 = ESP32Touch(Pin(touch3_pin), suppress=True)
    t3.press_func(lambda : mode3())

    while True:
        await asyncio.sleep(1)

asyncio.run(main())



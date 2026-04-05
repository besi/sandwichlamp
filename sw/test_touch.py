from machine import TouchPad, Pin
import time

touch_pin1 = TouchPad(Pin(14, mode=Pin.IN))
touch_pin2 = TouchPad(Pin(32, mode=Pin.IN))
touch_pin3 = TouchPad(Pin(4, mode=Pin.IN))

while True:
    touch_value1 = touch_pin1.read()
    touch_value2 = touch_pin2.read()
    touch_value3 = touch_pin3.read()    
    print(touch_value1, touch_value2, touch_value3)
    time.sleep_ms(500)

from machine import Pin, PWM
import asyncio
from primitives import ESP32Touch, Pushbutton
from  neopixel import NeoPixel
pixelCount = 44
np = NeoPixel(Pin(18), pixelCount)

touch1_pin = 14
touch2_pin = 32
touch3_pin = 4

button_a_pin = 34
button_b_pin = 33
button_c_pin = 39
button_d_pin = 36

enable12v_pin = 13

pwm_start = 610
pwm_end = 1020
pwm_steps = (pwm_end-pwm_start)/20
pwm = PWM(Pin(enable12v_pin), freq=1000)          # create a PWM object on a pin


mode_max = 2
mode = 1
intensity = 10 # 0 .. 20

def down():
    global intensity
    intensity = max(0, intensity -1 )
    print(f"Down {intensity}")

    update_mode(False)

def up():
    global intensity
    intensity = min(20, intensity + 1)
    print(f"Up {intensity}")

    update_mode(False)

def update_mode(modeChanged = True):
    global mode
    global intensity
    
    print(f"Mode = {mode}")
    if mode != 1 and modeChanged:
        pwm.duty(0)
    if mode == 1:
        if modeChanged and pwm.duty() > 1:
            pwm.duty(0)
        else:
            pwm.duty(int(intensity * pwm_steps)+pwm_start)
        

def change_mode():
    global mode
    if mode == mode_max:
        mode = 1
    else:
        mode += 1
    update_mode()
            
def button(number):
    print(f"Pressed Button #{number}")
    if number == 1:
        np.fill((25,0,0))
    elif number == 2:
        np.fill((0,25,0))
    elif number == 3:
        np.fill((0,0,25))
    elif number == 4:
        np.fill((0,0,0))
    np.write()
    
async def main():
    ESP32Touch.threshold(95)
    t1 = ESP32Touch(Pin(touch1_pin), suppress=True)
    t1.release_func(lambda : down())
    t2 = ESP32Touch(Pin(touch2_pin), suppress=True)
    t2.release_func(lambda : change_mode())
    t3 = ESP32Touch(Pin(touch3_pin), suppress=True)
    t3.release_func(lambda : up())

    pb1 = Pushbutton(Pin(button_a_pin, Pin.IN, Pin.PULL_UP))
    pb1.press_func(button, (1,))
    pb2 = Pushbutton(Pin(button_b_pin, Pin.IN, Pin.PULL_UP))
    pb2.press_func(button, (2,))
    pb3 = Pushbutton(Pin(button_c_pin, Pin.IN, Pin.PULL_UP))
    pb3.press_func(button, (3,))
    pb4 = Pushbutton(Pin(button_d_pin, Pin.IN, Pin.PULL_UP))
    pb4.press_func(button, (4,))

    update_mode()
    while True:
        await asyncio.sleep(1)

asyncio.run(main())

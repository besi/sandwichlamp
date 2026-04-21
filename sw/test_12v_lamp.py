from machine import PWM
import machine
import time

lamp = machine.Pin(13, machine.Pin.OUT)
lamp.on()
time.sleep(.5)
lamp.off()
time.sleep(.5)
lamp.on()
time.sleep(.5)

pwm = PWM(machine.Pin(13), freq=1000)          # create a PWM object on a pin

limit = 1020
while True:
    for x in range(480,limit):
        time.sleep(.003)
        pwm.duty(x)

    for x in reversed(range(480,limit)):
        time.sleep(.003)
        pwm.duty(x)

    pwm.duty(0)

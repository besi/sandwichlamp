from machine import PWM
import machine
import time

pwm = PWM(machine.Pin(13), freq=1000)          # create a PWM object on a pin


while True:
    for x in range(480,1023):
        time.sleep(.003)
        pwm.duty(x)

    for x in reversed(range(480,1023)):
        time.sleep(.003)
        pwm.duty(x)

    pwm.duty(0)

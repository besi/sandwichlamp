# import mip
# mip.install("github:robert-hh/BME280")

import machine
import bme280_float as bme280

i2c = machine.I2C(0, sda=machine.Pin(23), scl=machine.Pin(19))
bme = bme280.BME280(i2c=i2c)

print(bme.values)

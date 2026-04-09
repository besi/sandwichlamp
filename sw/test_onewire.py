# 1 Wire
from machine import Pin
import machine
import onewire, ds18x20
from onewire import OneWireError
dat = Pin(15, Pin.IN, Pin.PULL_UP) # New Pin 4
ds = ds18x20.DS18X20(onewire.OneWire(dat))
print(ds.scan())
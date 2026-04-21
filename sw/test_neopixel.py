from neopixel import NeoPixel

np = NeoPixel(machine.Pin(18),44)
np.fill((0,0,220))
np.write()

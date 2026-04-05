from neopixel import NeoPixel

np = NeoPixel(machine.Pin(18),1)
np.fill((10,10,0))
np.write()

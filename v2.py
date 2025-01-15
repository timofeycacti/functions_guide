def neostrip_Timofei(count: number):
    global curled
    for index in range(count):
        curled = randint(0, 3)
        strip.clear()
        strip.set_pixel_color(curled, neopixel.colors(NeoPixelColors.RED))
        for index2 in range(256):
            strip.clear()
            strip.set_pixel_color(curled, neopixel.colors(NeoPixelColors.RED))
            strip.set_brightness(255 - index2)
            strip.show()
            basic.pause(5)
        strip.show()
curled = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)

def on_forever():
    neostrip_Timofei(3)
    basic.pause(5000)
basic.forever(on_forever)

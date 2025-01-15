def neostrip_Timofei(count: number):
    for index in range(count):
        strip.clear()
        strip.set_pixel_color(randint(0, 3), neopixel.colors(NeoPixelColors.RED))
        strip.show()
        basic.pause(100)
        strip.clear()
        strip.show()
        basic.pause(10)
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
neostrip_Timofei(10)

def on_forever():
    basic.pause(100)
basic.forever(on_forever)

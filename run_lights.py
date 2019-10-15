from neopixel import *
from rpi_ws281x import *

import random
import soft_colours
import rainbow
import chase_light
import pulse

# LED Wire configuration:
LED_COUNT = 100  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53


class RunLights():

    def __init__(self):
        self.led_wire = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                                    LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.led_wire.begin()
        self.led_wire.show()

    def run_light_show(self):
        while True:
            next_show = random.randint(0, 2)
            next_show = 1
            if next_show == 0:
                soft_colours.run(self.led_wire, LED_COUNT, 30, 0.05, 200)
            if next_show == 1:
                soft_colours.run(self.led_wire, LED_COUNT, 30, 0.005, 200)
            elif next_show == 2:
                chase_light.run(self.led_wire, LED_COUNT, 30, 0.05, 10, 1)

            


if __name__ == "__main__":

    runningLights = RunLights()
    runningLights.run_light_show()

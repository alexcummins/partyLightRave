from rpi_ws281x import Adafruit_NeoPixel, Color
from Animations.Display import Display, Colour


class LEDDisplay(Display):

    # LED Wire configuration:
    LED_COUNT = 100  # Number of LED pixels.
    LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10  # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

    def __init__(self):
        self.led_wire = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA,
                                          self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        self.led_wire.begin()
        self.led_wire.show()

    def get_num_pixels(self):
        return self.LED_COUNT

    def set_pixel_colour(self, i: int, colour: Colour):
        self.led_wire.setPixelColor(i, Color(Colour.red, colour.green, colour.blue))

    def update(self):
        self.led_wire.show()

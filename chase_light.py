from neopixel import *
from rpi_ws281x import *
import time
import default_colours
import random
import math


class Chaser:

    def __init__(self, led_wire, led_num, brightness, colour):
        self.led_wire = led_wire
        self.brightness = brightness
        self.colour = colour
        self.led_num = led_num

    def set_brightness(self, new_brightness):
        # brightness is a fraction of 1
        self.brightness = new_brightness

    def divide(self, division_amount):
        self.brightness /= division_amount
        if self.brightness < 10:
            return False

    def set_colour(self, new_colour):
        self.colour = list(new_colour)

    def push_to_led(self):
        for i in range(3):
            self.colour[i] * brightness
        self.led_wire.setPixelColour(self.led_num, Color(self.colour))


def run(led_wire, string_length, running_time, wait_time, num_chasers):
    start_time = time.time()

    # chaser setup
    chaser_list = []
    chaser_displacement = math.floor(string_length / num_chasers)
    for i in range(num_chasers):
        chaser_list.append(Chaser(led_wire, i * chaser_displacement,
                                  1, default_colours.white))

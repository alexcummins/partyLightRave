from neopixel import *
from rpi_ws281x import *
from default_colours import *
import time
import random
import math


def run(led_wire, string_length, running_time, transition_steps):
    start_time = time.time()
    current_colour = list(red)
    transition_steps = 10

    colour_list = [red, orange, yellow, light_green, green,
                   turquoise, blue, indigo, violet, pink]
    while (start_time - time.time()) < running_time:
        new_colour = random.choice(colour_list)
        max_colour_diff = 0
        change_per_transition = [0, 0, 0]

        for i in range(3):
            change_per_transition[i] = math.floor(abs(new_colour[i] - colour[i]) / transition_steps)

        while new_colour != tuple(current_colour):
            for i in range(3):
                if abs(new_colour[i] - current_colour[i]) < change_per_transition[i]:
                    current_colour[i] = new_colour[i]
                elif new_colour[i] < current_colour[i]:
                    new_colour[i] += change_per_transition[i]
                elif new_colour[i] > current_colour[i]:
                    new_colour[i] -= change_per_transition[i]
            led_wire.setPixelColour(1, Color(tuple(current_colour)))
            led_wire.show()
            # add function to set colour of all LEDs HERE
            time.sleep(0.025)


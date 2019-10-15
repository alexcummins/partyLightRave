from neopixel import *
from rpi_ws281x import *
from default_colours import *
import time
import random
import math

DIMINISHING_BRIGHTNESS = 0.8

def run(led_wire, string_length, running_time, sleep_time, num_pulses, time_between_pulse, colour, staggered):
    ## TODO
    
    # start_time = time.time()

    # if colour == "random":
    #     colour_list = [red, dim_orange, dim_yellow, dim_light_green,
    #                    green, dim_turquoise, blue, dim_pink]
    # current_colour = list(random.choice(colour_list))

    # while (time.time() - start_time) < running_time:
    #     pulse_start = random.randint(0, string_length)
    #     led_wire.setPixelColor(pulse_start, Color(current_colour[1],
    #                             current_colour[0], current_colour[2]))
    #     for i in (1, 2, 3):
    #         for c in current_colour:
    #             c * DIMINISHING_BRIGHTNESS
    #         for j in (-i, i):
    #             if pulse_start + j > 0 or pulse_start + j < string_length:
    #                 led_wire.setPixelColor(pulse_start - j, Color(current_colour[1],
    #                                     current_colour[0], current_colour[2]))
                



            # for i in range(100):
                # led_wire.setPixelColor(i, Color(current_colour[1],
                                #  current_colour[0], current_colour[2]))
            # led_wire.show()
            # time.sleep(sleep_time)

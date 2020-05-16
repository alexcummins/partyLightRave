from Animations import Display
from Animations.default_colours import *
import time
import random
import math

BRIGHTNESS_CUTOFF = 0.1


class Chaser:

    def __init__(self, display: Display, led_num, max_brightness, colour, trailer):
        self.display: Display = display
        self.brightness = max_brightness
        self.colour = list(colour)
        self.led_num = led_num
        self.trailer: Chaser = trailer

    def set_brightness(self, new_brightness):
        # brightness is a fraction of 1
        self.brightness = new_brightness

    def divide(self, division_amount):
        if self.trailer is not None:
            self.trailer.divide(division_amount)
            if self.trailer.get_brightness() < BRIGHTNESS_CUTOFF:
                self.trailer.set_colour((0, 0, 0))
                self.trailer.push_to_led()
                del self.trailer
        self.brightness /= division_amount

    def set_colour(self, new_colour):
        self.colour = list(new_colour)

    def set_trailer(self, trailer):
        self.trailer = trailer

    def push_to_led(self):
        for i in range(3):
            self.colour[i] = math.floor(self.colour[i] * self.brightness)
        if self.trailer is not None:
            self.trailer.push_to_led()
        if self.led_num > 0 or self.led_num < self.display.get_num_pixels():
            self.display.set_pixel_colour(self.led_num, Colour(self.colour[1],
                                                               self.colour[0], self.colour[2]))

    def get_led_num(self):
        return self.led_num

    def get_colour(self):
        return self.colour

    def get_brightness(self):
        return self.brightness


class ChaseLight:

    @staticmethod
    def run(display: Display, running_time, sleep_time, chaser_chance, regular, colours, reverse):
        # Currently overlapping flashes, need to change
        start_time = time.time()

        if colours == "random":
            colour_list = all_colours
        else:
            colour_list = colours

        if reverse:
            next = -1
            insert_pos = display.get_num_pixels
        else:
            next = 1
            insert_pos = 0

        # chaser setup
        chaser_list = [Chaser(display, insert_pos,
                              1, random.choice(colour_list), 0)]
        num_steps_gone = 0

        while (time.time() - start_time) < running_time:
            if num_steps_gone > 10:
                if regular:
                    chaser_list.append(Chaser(display, insert_pos,
                                              1, random.choice(colour_list), 0))
                else:
                    if random.randint(0, 100) <= chaser_chance:
                        chaser_list.append(Chaser(display, insert_pos,
                                                  1, random.choice(colour_list), 0))
                num_steps_gone = 0
            for chaser in chaser_list:
                chaser.push_to_led()
                chaser.divide(1.25)

            display.update()
            time.sleep(sleep_time)

            try:
                for i in range(len(chaser_list)):
                    if (chaser_list[i].get_led_num() + 1) > display.get_num_pixels() + 10 or (
                            chaser_list[i].get_led_num() - 1) < -10:
                        del chaser_list[i]
                    else:
                        chaser_list.insert(0, Chaser(display, chaser_list[i].get_led_num() + next, 1,
                                                     chaser_list[i].get_colour(), chaser_list[i]))
                        del chaser_list[i + 1]  # because inserted a new element before
            except IndexError:
                continue
            num_steps_gone += 1

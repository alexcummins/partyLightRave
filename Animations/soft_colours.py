from Animations.Display import Display
from Animations.default_colours import Colour
from Animations.default_colours import all_colours
import time
import random
import math


class SoftColours:

    @staticmethod
    def run(display: Display, running_time, sleep_time, transition_steps):
        start_time = time.time()

        current_colour = list(random.choice(all_colours))
        while (time.time() - start_time) < running_time:
            new_colour = list(random.choice(all_colours))
            change_per_transition = [0, 0, 0]

            for i in range(3):
                change_per_transition[i] = math.floor(abs(new_colour[i] - current_colour[i]) / transition_steps)
                if change_per_transition[i] == 0:
                    change_per_transition[i] = 1

            # print("Change per transition: ", change_per_transition)

            while new_colour != current_colour:
                for i in range(3):
                    if abs(new_colour[i] - current_colour[i]) < change_per_transition[i]:
                        current_colour[i] = new_colour[i]
                    elif new_colour[i] < current_colour[i]:
                        current_colour[i] -= change_per_transition[i]
                    elif new_colour[i] > current_colour[i]:
                        current_colour[i] += change_per_transition[i]
                # print(current_colour)
                # for i in current_colour:
                #     i / 2
                #     i = math.floor(i)
                for i in range(100):
                    display.set_pixel_colour(i, Colour(current_colour[1],
                                                       current_colour[0], current_colour[2]))
                display.update()
                time.sleep(sleep_time)

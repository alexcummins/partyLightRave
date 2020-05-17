from Animations.Display import Display
from Animations.animation import Animation
from Animations.default_colours import Colour
from Animations.default_colours import all_colours
import time
import random
import math


class SoftColours(Animation):

    def __init__(self, display: Display, running_time: int, sleep_time: float, transition_steps: int):

        super().__init__(display)
        self.display = display
        self.running_time = running_time
        self.sleep_time = sleep_time
        self.transition_steps = transition_steps

    def run(self):
        start_time = time.time()

        current_colour: Colour = (random.choice(all_colours))
        while (time.time() - start_time) < self.running_time:
            new_colour: Colour = random.choice(all_colours)
            change_per_transition = [0, 0, 0]

            for i in range(3):
                change_per_transition[i] = math.floor(abs(new_colour[i] - current_colour[i]) / self.transition_steps)
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
                    self.display.set_pixel_colour(i, Colour(current_colour[1],
                                                            current_colour[0], current_colour[2]))
                self.display.update()
                time.sleep(self.sleep_time)

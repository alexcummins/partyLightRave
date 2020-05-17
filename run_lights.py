import random
from Animations import Display, LEDDisplay
from Animations.chase_light import ChaseLight
from Animations.default_colours import *
from Animations.soft_colours import SoftColours


# TODO: Need to make the animations implement run. Make run not have any parameters,
# whereas instead the classes take in parameters on init, and then run just starts their show
# on display.


class RunLights:
    RUNNING_TIME = 30
    CHASER_CHANCE = 10

    def __init__(self, display: Display):
        self.display = display

    def run_light_show(self):

        while True:
            next_show = random.randint(0, 5)
            fast = random.choice((True, False))
            if fast:
                chase_sleep = 0.02
            else:
                chase_sleep = 0.08
            if next_show == 0:
                if fast:
                    SoftColours(self.display, self.RUNNING_TIME, 0.008, 100).run()
                else:
                    SoftColours(self.display, self.RUNNING_TIME, 0.1, 500).run()
            elif next_show == 1:
                    SoftColours(self.display, self.RUNNING_TIME, 0.05, 50).run()
            elif next_show == 2:
                ChaseLight(self.display, self.RUNNING_TIME, chase_sleep,
                           self.CHASER_CHANCE, regular=True, colours="random", reverse=False).run()
            elif next_show == 3:
                ChaseLight(self.display, self.RUNNING_TIME, chase_sleep,
                           self.CHASER_CHANCE, regular=True, colours="random", reverse=True).run()
            elif next_show == 4:
                ChaseLight(self.display, self.RUNNING_TIME, chase_sleep,
                           self.CHASER_CHANCE, regular=True, colours=[random.choice(all_colours)],
                           reverse=False).run()
            elif next_show == 5:
                ChaseLight(self.display, self.RUNNING_TIME, chase_sleep,
                           self.CHASER_CHANCE, regular=True, colours=[random.choice(all_colours)],
                           reverse=True).run()


if __name__ == "__main__":
    runningLights = RunLights(LEDDisplay.LEDDisplay())
    runningLights.run_light_show()

import abc

from Animations.default_colours import Colour


class Display(abc.ABC):

    @abc.abstractmethod
    def get_num_pixels(self) -> int:
        pass

    @abc.abstractmethod
    def set_pixel_colour(self, i: int, colour: Colour):
        pass

    @abc.abstractmethod
    def update(self):
        pass

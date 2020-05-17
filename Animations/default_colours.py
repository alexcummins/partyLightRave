from dataclasses import dataclass, astuple


@dataclass
class Colour:
    red: int
    green: int
    blue: int

    def __getitem__(self, item) -> int:
        if item == 0:
            return self.red
        elif item == 1:
            return self.green
        elif item == 2:
            return self.blue

    def __setitem__(self, key, value):
        if key == 0:
            red = value
        if key == 1:
            green = value
        if key == 2:
            blue = value


# Some default colours, in tuple form RGB

white = Colour(255, 255, 255)
dim_white = Colour(100, 100, 100)
red = Colour(255, 0, 0)
orange = Colour(255, 127, 0)
dim_orange = Colour(130, 40, 0)
yellow = Colour(255, 255, 0)
dim_yellow = Colour(100, 100, 0)
light_green = Colour(128, 255, 0)
dim_light_green = Colour(100, 150, 0)
green = Colour(0, 255, 0)
dim_turquoise = Colour(0, 150, 150)
turquoise = Colour(0, 255, 255)
blue = Colour(0, 0, 255)
violet = Colour(148, 0, 211)
pink = Colour(255, 0, 127)
dim_pink = Colour(70, 0, 30)

all_colours: Colour = [white, red, orange, yellow, light_green, green,
                       turquoise, blue, violet, pink]

import abc

from Animations import Display


class Animation:
    display: Display

    def __init__(self, display: Display):
        self.display = display

    def set_display(self, display: Display):
        self.display = display

    @abc.abstractmethod
    def run(self):
        pass

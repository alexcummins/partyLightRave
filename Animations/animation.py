import abc

from Animations import Display


class Animation:
    @abc.abstractmethod
    def run(self, display: Display, params):
        pass

from abc import ABC, abstractmethod


class PrintInterface(ABC):
    @abstractmethod
    def print_generic(self):
        pass

    @abstractmethod
    def print_name(self, name):
        pass

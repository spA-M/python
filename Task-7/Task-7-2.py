from abc import ABC, abstractmethod


class Fabric(ABC):

    def __init__(self, v):
        self.v = v

    @abstractmethod
    def calc(self):
        pass

    @property
    def size(self):
        return f"Общий расход ткани равен: {self.v / 6.5 + 0.5} {self.v * 2 + 0.3}"


class Coat (Fabric):

    def calc(self):
        return self.v / 6.5 + 0.5

class Suit (Fabric):

    def calc(self):
        return self.v * 2 + 0.3

a = Coat(46)
b = Suit(180)


print(f"Расход ткани для пальто, при данных параметрах, равен: {round(a.calc())}")
print(f"Расход ткани для костюма, при данных параметрах, равен: {round(b.calc())}")
print(f"Общий расход ткани, при данных параметрах, равен: {round(b.calc()) + round(a.calc())}")

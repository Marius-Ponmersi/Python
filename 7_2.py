from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def rashod(self):
        pass

class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def rashod(self):
        print(f'Расход ткани для пальто размера {self.V} равен: {self.V / 6.5 + 0.5}')

class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def rashod(self):
        print(f'Расход ткани для костюма роста {self.H} равен: {2 * self.H + 0.3}')

co = Coat(52)
su = Suit(2)
co.rashod
su.rashod

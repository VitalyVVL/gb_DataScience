from abc import ABC,abstractmethod


class Clothes(ABC):
    exp_sum = 0

    @abstractmethod
    def exp(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.name = 'Пальто'
        Clothes.exp_sum+=self.exp

    @property
    def exp(self):
        return float(f'{(self.size/6.5 +0.5):.02f}')

    def __str__(self):
        return f'{self.name}: {self.size:.02f}, расход ткани {self.exp} \n расход всего : {self.exp_sum:.02f}'


class Suit(Clothes):
    def __init__(self, height):
       self.height = height
       self.name = 'Кастюм'
       Clothes.exp_sum += self.exp


    @property
    def exp(self):
        return float(f'{(2*self.height + 0.3):.02f}')


    def __str__(self):
          return f'{self.name}: {self.height}, расход ткани {self.exp:.02f} \n расход всего : {self.exp_sum:.02f}'



сoat_1 = Coat(60)
print(сoat_1)
suit_1 = Suit(180)
print(suit_1)

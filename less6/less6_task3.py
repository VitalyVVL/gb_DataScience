
class Worker:
    def __init__(self, name, surname, position, wage,bonus):
        self.name = name
        self.surname = surname
        self.position =position
        self._income = {'wage':int(wage), 'bonus':int(bonus)}


class Position(Worker):
   def get_full_name(self):
    return f'{self.name} {self.surname}'

   def get_full_profit(self):
     return f'{sum(self._income.values())}'

manager = Position('Иван', 'Иванов', 'директор','20000','30000')
print(f'{manager.position}')
print(f'{manager.get_full_profit()}')
print(f'{manager.get_full_name()}')



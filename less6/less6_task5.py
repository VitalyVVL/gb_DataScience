class Stationery:
    def __init__(self, title = 'Неопределено'):
        self.title = title

    def draw(self):
        print(f'Начинаю рисовать! {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Начинаю рисовать! {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Начинаю рисовать! {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Начинаю рисовать! {self.title}')

pen = Pen('ручка')
pen.draw()

Pencil  = Pencil('карандаш')
Pencil.draw()

Handle = Handle('маркер')
Handle.draw()





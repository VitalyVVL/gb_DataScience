class Car:
    is_police = False

    def __init__(self, name, color, speed):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self, speed= 30):
        self.speed=speed
        print(f'{self.name} машина поехала со скоростью {self.speed}')

    def stop(self):
        self.speed=0
        print(f'{self.name} машина остановилась')

    def turn(self, direction):
        print(f'{self.name}: Машина воернула: {"налево" if direction==0 else "направо"}')

    def show_sreed(self):
        print(f'{self.name}: Скорость автомобиля: {self.speed}')


class TownCar(Car):
    def show_sreed(self):
      if self.speed>60:
          over_speed = self.speed - 60
          print(f'{self.name}: Скорость автомобиля: {self.speed}  превышение скорости на: {over_speed}')
      else:
          print(f'{self.name}: Скорость автомобиля {self.speed}')
          #f'{f"Превышение скорости на " if self.speed > 60}')

class SportCar(Car):
     pass


class WorkCar(Car):
    def show_sreed(self):
        if self.speed > 40:
            over_speed = self.speed - 40
            print(f'{self.name}: Скорость автомобиля: {self.speed}  превышение скорости на: {over_speed}')
        else:
            print(f'{self.name}: Скорость автомобиля {self.speed}')
            # f'{f"Превышение скорости на " if self.speed > 60}')

class PoliceCar(Car):
    is_police = True


police_car = PoliceCar('Волга','сний', 80)
police_car.go()
police_car.show_sreed()
police_car.turn(1)
police_car.stop()
print()

WorkCar = WorkCar('ЗИЛ','сний', 40)
WorkCar.go()
WorkCar.show_sreed()
WorkCar.go(80)
WorkCar.show_sreed()
WorkCar.turn(0)
WorkCar.stop()
print()

TownCar = TownCar('ЗИЛ','сний', 60)
TownCar.go()
TownCar.show_sreed()
TownCar.go(100)
TownCar.show_sreed()
TownCar.turn(0)
TownCar.stop()
print()

SportCar = SportCar('Волга','сний', 80)
SportCar.go()
SportCar.show_sreed()
SportCar.turn(1)
SportCar.stop()
print()








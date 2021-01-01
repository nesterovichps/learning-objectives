# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
from self import self


class Car():

    def __init__(self,speed_car,color_car,name_car):
        self.speed=speed_car
        self.color=color_car
        self.name=name_car
        self.is_police = False

    def go(self):
        print('машина поехала')
    def stop(self):
        print('машина остановилась')
    def turn(self,direction):
        if direction =='left':
            print('Машина повернула налево')
        elif direction == 'right':
            print('машина повернула направо')
        else:
            self.turn(input('Куда повернуть?'))
    def show_me(self):
        print(f'Модель машины {self.name}, цвет {self.color}, скорость {self.speed}, полицейская {self.is_police}')
class TownCar(Car):
    pass

class SportCar(Car):
    pass
class WorkCar(Car):
    pass
class PoliceCar(Car):
    def __init__(self,speed_car,color_car,name_car):
        super().__init__(speed_car,color_car,name_car)
        self.is_police=True

town_car=TownCar(90,'white','bmw')
town_car.show_me()
town_car.go()
town_car.turn('left')
town_car.turn('right')
town_car.stop()
sport_car=SportCar(200,'black','mersedes')
sport_car.show_me()
sport_car.go()
sport_car.turn('left')
sport_car.turn('right')
sport_car.stop()
work_car=WorkCar(60,'yellow','maz')
work_car.show_me()
work_car.go()
work_car.turn('left')
work_car.turn('right')
work_car.stop()
police_car=PoliceCar(120,'blue','shkoda')
police_car.show_me()
police_car.go()
police_car.turn('left')
police_car.turn('right')
police_car.stop()

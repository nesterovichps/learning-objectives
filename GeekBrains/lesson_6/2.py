# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car():

    def __init__(self, speed_car, color_car, name_car):
        self.speed = speed_car
        self.color = color_car
        self.name = name_car
        self.is_police = False

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        if direction == 'left':
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
    def __init__(self, speed_car, color_car, name_car):
        super().__init__(speed_car, color_car, name_car)
        self.is_police = True


town_car = TownCar(90, 'white', 'bmw')
sport_car = SportCar(200, 'black', 'mersedes')
work_car = WorkCar(60, 'yellow', 'maz')
police_car = PoliceCar(120, 'blue', 'shkoda')

for car in [town_car, sport_car, work_car, police_car]:
    car.show_me()
    car.go()
    car.turn('left')
    car.turn('right')
    car.stop()

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка
class Toy:
    def __init__(self):
        self.type_toy = 'Template'
        self.color_toy = 'white'
        self.name_toy = ''
        self.materials = False
        self.sew = False


class MarvelToy(Toy):
    def __init__(self):
        super().__init__()
        self.logo = 'Marvel'


class DsToy(Toy):
    def __init__(self):
        super().__init__()
        self.logo = 'DS'


class Dog(Toy):
    def __init__(self):
        super().__init__()
        self.wool = True
        self.tail = True


class Cat(Toy):
    def __init__(self):
        super().__init__()
        self.wool = True
        self.tail = True


class CreatedToy:
    def __init__(self, name_toy, color_toy, type_toy):
        if type_toy == 'Marvel toy':
            self.toy = MarvelToy()
        elif type_toy == 'DS toy':
            self.toy = DsToy()
        elif type_toy == 'cat':
            self.toy = Cat()
        elif type_toy == 'dog':
            self.toy = Dog()
        else:
            self.toy = Toy()
        # self._show_status()
        self.pay_materials(name_toy)
        # self._show_status()
        self.sewing(type_toy)
        # self._show_status()
        self.painting(color_toy)
        self._show_status()
        print()
        self.return_result()

    def _show_status(self):
        print('Status Toy')
        print(
            f'Игрушка. Тип {self.toy.type_toy} цвет {self.toy.color_toy} название {self.toy.name_toy} материал {self.toy.materials} изготовлена {self.toy.sew}')

    def pay_materials(self, name_toy):
        self.toy.name_toy = name_toy
        print(f'Paying materials for {self.toy.name_toy}')
        self.toy.materials = True

    def sewing(self, type_toy):
        print(f'Sewing toy {self.toy.name_toy}')
        self.toy.sew = True
        self.toy.type_toy = type_toy

    def painting(self, color_toy):
        print(f'Painting {self.toy.name_toy}')
        self.toy.color_toy = color_toy

    def return_result(self):
        return self.toy


pauk = CreatedToy('Pauk', 'red', 'Marvel toy')
print(pauk.toy.name_toy, type(pauk.toy))
betmen = CreatedToy('Betmen', 'black', 'DS toy')
print(betmen.toy.name_toy, type(betmen.toy))
halk = CreatedToy('Halk', 'green', 'Marvel toy')
print(halk.toy.name_toy, type(halk.toy))
cat = CreatedToy('Bullet', 'grey', 'cat')
print(cat.toy.name_toy, type(cat.toy))
dog = CreatedToy('Lord', 'redhead', 'dog')
print(dog.toy.name_toy, type(dog.toy))

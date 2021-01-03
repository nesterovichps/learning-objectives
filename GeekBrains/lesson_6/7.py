# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Toy:
    def __init__(self):
        self.type_toy = 'Template'
        self.color_toy = 'white'
        self.name_toy = ''
        self.materials = False
        self.sew = False


class CreatedToy:
    def __init__(self, name_toy, color_toy, type_toy):
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
halk = CreatedToy('Halk', 'green', 'Marvwl toy')
print(halk.toy.name_toy, type(halk.toy))
cat = CreatedToy('Bullet', 'grey', 'cat')
print(type(cat.toy.name_toy, cat.toy))
dog = CreatedToy('Lord', 'redhead', 'dog')
print(dog.toy.name_toy, type(dog.toy))

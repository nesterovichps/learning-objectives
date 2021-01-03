# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random
import time


class Person:
    def __init__(self, health, damage, armor):
        self.name = None
        self.health = health + random.randint(0, 500)
        self.min_damage = damage
        self.max_damage = damage + random.randint(0, 50)
        self.armor = armor

    def _get_damage(self, damage):
        get_damage = round(damage * self.armor)
        resist = damage - get_damage
        self.health = self.health - damage
        print(f'Игрок {self.name} получил {get_damage} урона, отражено {resist} ед. урона.')
        print()

    def _attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        print(f'Игрок {self.name} нанес {damage} урона.')
        return damage


class Player(Person):
    def __init__(self, health, damage, armor, critical_damage, chance_critical_damage):
        super().__init__(health, damage, armor)
        self.name = 'Player'
        self.critical_damage = critical_damage
        self.chance_critical_damage = chance_critical_damage

    def _attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        if self._critical_status()[0]:
            damage = damage * critical_damage / 100
            print(f'Игрок {self.name} нанес КРИТИЧЕСКИЙ УРДАР {damage} ед урона.')
        else:
            print(f'Игрок {self.name} нанес {damage} урона.')
        return damage

    def _critical_status(self):
        return random.choices([True, False], weights=[self.chance_critical_damage, 100 - self.chance_critical_damage])


class Enemy(Person):
    def __init__(self, health, damage, armor, chance_miss):
        super().__init__(health, damage, armor)
        self.name = 'Enemy'
        self.chance_miss = chance_miss

    def _get_damage(self, damage):
        if self._miss_status()[0]:
            print(f'Игрок {self.name} уклонился, получил 0 урона.')
            print()
        else:
            get_damage = round(damage * self.armor)
            resist = damage - get_damage
            self.health = self.health - damage
            print(f'Игрок {self.name} получил {get_damage} урона, отражено {resist} ед. урона.')
            print()

    def _miss_status(self):
        return random.choices([True, False], weights=[self.chance_miss, 100 - self.chance_miss])


class StartGame():
    def __init__(self, health_player, damage_player, armor_player, critical_damage, chance_critical_damage,
                 health_enemy, damage_enemy, armor_enemy, chance_miss):
        print()
        print('Игра началась \n')

    def start_game(self, ):
        self._init_person()
        if random.randint(1, 2) == 1:
            now_player = self.player
            other_player = self.enemy
        else:
            now_player = self.enemy
            other_player = self.player
        win = self._game(now_player, other_player)
        print(win.name)

    def _game(self, now_player, other_player):
        while self.player.health > 0 and self.enemy.health > 0:
            damage = now_player._attack()
            other_player._get_damage(damage)
            time.sleep(0.1)
            self.show_person(other_player)
            now_player, other_player = other_player, now_player
        if self.player.health > 0:
            return self.player
        return self.enemy

    def _init_person(self):
        self.player = Player(health_player, damage_player, armor_player, critical_damage, chance_critical_damage)
        self.enemy = Enemy(health_enemy, damage_enemy, armor_enemy, chance_miss)
        print(f'Игрок {self.player.name} Создан.')
        self.show_person(self.player)
        print(f'Игрок {self.enemy.name} Создан.')
        self.show_person(self.enemy)

    def show_person(self, person):
        print('===============')
        try:
            print(f'Игрок {person.name} \n\
            Здоровье {person.health} \n\
            Атака ({person.min_damage} - {person.max_damage}) \n\
            Броня {person.armor}\n\
            Критический урон {person.critical_damage}\n\
            Шанс критического урона {person.chance_critical_damage}%')
        except:
            print(f'Игрок {person.name} \n\
            Здоровье {person.health} \n\
            Атака ({person.min_damage} - {person.max_damage}) \n\
            Броня {person.armor}\n\
            Шанс промаха {person.chance_miss}%')
        print('===============')
        print()


health_player = 600
health_enemy = 600
damage_player = 20
damage_enemy = 20
armor_player = 2.1
armor_enemy = 1.2
critical_damage = 200
chance_critical_damage = 20
chance_miss = 50
game = StartGame(health_player, damage_player, armor_player, critical_damage, chance_critical_damage,
                 health_enemy, damage_enemy, armor_enemy, chance_miss)
game.start_game()

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
import random


def attack(person1, person2):
    print(
        f'{person1["name"]} : {person1["health"]} health damage {person1["damage"] - person1["delta_damage"]} - {person1["damage"] + person1["delta_damage"]}')
    print(
        f'{person2["name"]} : {person2["health"]} health damage {person2["damage"] - person2["delta_damage"]} - {person2["damage"] + person2["delta_damage"]}')
    print()

    while person1['health'] >= 0 and person2['health'] >= 0:
        damage_1 = random.randint(person1["damage"] - person1["delta_damage"],
                                  person1["damage"] + person1["delta_damage"])
        damage_2 = random.randint(person2["damage"] - person2["delta_damage"],
                                  person2["damage"] + person2["delta_damage"])
        person1["health"], person2["health"] = person1["health"] - damage_2, person2["health"] - damage_1
        print(
            f'{person1["name"]} нанес {damage_1} урона. Получил {damage_2} урона. {person1["health"]} health damage {person1["damage"] - person1["delta_damage"]} - {person1["damage"] + person1["delta_damage"]}')
        print(
            f'{person2["name"]} нанес {damage_2} урона. Получил {damage_1} урона. {person2["health"]} health damage {person2["damage"] - person2["delta_damage"]} - {person2["damage"] + person2["delta_damage"]}')
        print()
    print(f'{person1["name"]} and {person2["name"]} dead.' if person1["health"] <= 0 and person2[
        "health"] <= 0 else f'Win {person1["name"]}' if person1["health"] > 0 else f'Win {person2["name"]}')


name_1 = input('Input name Plaer 1 ')
name_2 = input('Input name Plaer 2 ')
health_1 = 500
health_2 = 800
delta_health = 70
damage_1 = 40
damage_2 = 30
delta_damage = 30

player = dict(name=name_1,
              health=random.randint(health_1 - delta_health, health_1 + delta_health),
              damage=(damage_1), delta_damage=delta_damage)
enemy = dict(name=name_2,
             health=random.randint(health_2 - delta_health, health_2 + delta_health),
             damage=(damage_2),
             delta_damage=delta_damage)

attack(player, enemy)

# Задание - 2
# + Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# + Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# + Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# + Сохраните эти сущности, полностью, каждую в свой файл,
# + в качестве названия для файла использовать name, расширение .txt
# + Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# + после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# + пока у одного из них health не станет меньше или равен 0.
# + После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random


def start_game(name_1, name_2):
    player_1, player_2 = read_from_file(name_1, name_2)
    win = attack(player_1, player_2)
    print(f'WIN {win["name"]}!!!  {win["health"]} health left')


def armor_resist(player):
    damage = (random.randint(player["damage"] - player["delta_damage"], player["damage"] + player["delta_damage"])) / \
             player['armor']
    return damage


def attack(person1, person2):
    print(
        f'{person1["name"]} : {person1["health"]} health damage {person1["damage"] - person1["delta_damage"]} - {person1["damage"] + person1["delta_damage"]} armor {person1["armor"]}')
    print(
        f'{person2["name"]} : {person2["health"]} health damage {person2["damage"] - person2["delta_damage"]} - {person2["damage"] + person2["delta_damage"]} armor {person2["armor"]}')
    print()

    while person1['health'] >= 0 and person2['health'] >= 0:
        damage_1 = armor_resist(person1)
        damage_2 = armor_resist(person2)
        person1["health"], person2["health"] = person1["health"] - damage_2, person2["health"] - damage_1
        print(
            f'{person1["name"]} нанес {damage_1} урона. Получил {damage_2} урона. {person1["health"]} health damage {person1["damage"] - person1["delta_damage"]} - {person1["damage"] + person1["delta_damage"]} armor {person1["armor"]}')
        if person2['health'] > 0:
            print(
                f'{person2["name"]} нанес {damage_2} урона. Получил {damage_1} урона. {person2["health"]} health damage {person2["damage"] - person2["delta_damage"]} - {person2["damage"] + person2["delta_damage"]} armor {person2["armor"]}')
            print()
            if person1['health'] <= 0:
                return person2
    return person1


def write_in_file(plaer_1, plaer_2):
    with open('{}.txt'.format(plaer_1['name']), 'w', encoding='utf-8') as file_1:
        file_1.write(str(plaer_1).replace(', ', '\n').replace("'", "")[1:-1])
    with open('{}.txt'.format(plaer_2['name']), 'w', encoding='utf-8') as file_2:
        file_2.write(str(plaer_2).replace(', ', '\n').replace("'", "")[1:-1])


def read_from_file(name_1, name_2):
    with open('{}.txt'.format(name_1), 'r', encoding='utf-8') as file_1:
        plaer_1 = dict()
        for line in file_1:
            line = line.split('\n')  # из строки получаем список
            line = line[0]  # избавляемся от последнего элемента (\n)
            line = line.split(': ')  # разделяем данные
            if line[0] == 'name':
                plaer_1[line[0]] = line[1]
            else:
                plaer_1[line[0]] = float(line[1])

    with open('{}.txt'.format(name_2), 'r', encoding='utf-8') as file_2:
        plaer_2 = dict()
        for line in file_2:
            line = line.split('\n')  # из строки получаем список
            line = line[0]  # избавляемся от последнего элемента (\n)
            line = line.split(': ')  # разделяем данные
            if line[0] == 'name':
                plaer_2[line[0]] = line[1]
            else:
                plaer_2[line[0]] = float(line[1])

    return plaer_1, plaer_2


# def attack

name_1 = 'Vasiliy'
name_2 = 'Sergey'
health_1 = 500
health_2 = 800
delta_health = 70
damage_1 = 40
damage_2 = 30
delta_damage = 20
armor_1 = 1.2
armor_2 = 1.2
player = dict(name=name_1,
              health=random.randint(health_1 - delta_health, health_1 + delta_health),
              damage=(damage_1), delta_damage=delta_damage, armor=armor_1)

enemy = dict(name=name_2,
             health=random.randint(health_2 - delta_health, health_2 + delta_health),
             damage=(damage_2), delta_damage=delta_damage, armor=armor_2)

write_in_file(player, enemy)
player = enemy = ''
start_game(name_1, name_2)

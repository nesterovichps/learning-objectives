# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def calculation(profil):
    norm_hour = int(worker[-3]) / int(worker[-2])
    if int(worker[-1]) < int(worker[-2]):
        print(
            f'{worker[1]} {worker[0]} отработал {worker[-1]} часов, норма часов {worker[-2]}. Оклад {worker[-3]}. В текущем месяце заработная плата составила {round(norm_hour * int(worker[-1]), 2)}')
    elif int(worker[-1]) == int(worker[-2]):
        print(
            f'{worker[1]} {worker[0]} отработал норму {worker[-2]} часов. Оклад {worker[-3]}. В текущем месяце заработная плата составила {worker[-3]}')
    else:
        over_the_norm = int(worker[-1]) - int(worker[-2])
        print(
            f'{worker[1]} {worker[0]} отработал {worker[-1]} часов, норма часов {worker[-2]}. Оклад {worker[-3]}. В текущем месяце переработка {over_the_norm} часов. Заработная плата составила {int(worker[-3]) + over_the_norm * norm_hour * 2}')


worker_list = []

with open('data/workers', 'r', encoding='utf-8') as workers:
    for line in workers.readlines()[1:]:
        line = line.strip().split()
        line.remove(line[3])
        worker_list.append(line)

with open('data/hours_of', 'r', encoding='utf-8') as hour:
    for line in hour.readlines()[1:]:
        line = line.strip().split()
        for list in worker_list:
            if line[0] in list and line[1] in list:
                list.append(line[2])
for worker in worker_list:
    calculation(worker)

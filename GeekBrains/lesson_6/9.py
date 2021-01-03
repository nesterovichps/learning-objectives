# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Person:
    def __init__(self, line):
        self.first_name,self.family_name,self.salary,self.post,self.rate_hours=line.strip().split()
        self.salary=int(self.salary)
        self.rate_hours=int(self.rate_hours)
class Company:
    list_person = []
    def __init__(self):
        pass

    def add_person(self, line):
        self.list_person.append(Person(line))

    def add_hour(self, line):
        first_name, family_name, hours_worked=line.strip().split()
        hours_worked=int(hours_worked)
        for person in self.list_person:
            if person.first_name == first_name and person.family_name == family_name:
                person.hours_worked = hours_worked


    def calkulate(self,person):
        if person.rate_hours<person.hours_worked:
            part1=person.salary
            part2=(person.hours_worked-person.rate_hours)*(person.salary/person.rate_hours)*2
            person.salary_thish_month=part1+part2
        else:
            person.salary_thish_month=person.salary/person.rate_hours*person.hours_worked
    def get_all_salary_in_month(self):
        for person in self.list_person:
            self.calkulate(person)
            self.show_person(person)
    def show_person(self,person):
        print(f'Сотрудник {person.family_name} {person.first_name} норма часов {person.rate_hours} заработная плата {person.salary} отработано часов в текущем месяце {person.hours_worked} получил {round(person.salary_thish_month,2)} рублей.')


company = Company()
with open('data/workers', 'r', encoding='utf-8') as file:
    for line in file.readlines()[1:]:
        company.add_person(line)

with open('data/hours_of', 'r', encoding='utf-8')as file:
    for line in file.readlines()[1:]:
        company.add_hour(line)
company.get_all_salary_in_month()
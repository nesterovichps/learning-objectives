# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class AddStudent:
    def __init__(self, study_in_class, name, mather, father):
        self.study_in_class = study_in_class
        self.name = name
        self.name_mather = mather
        self.name_father = father


class AddTeacher:
    def __init__(self, lesson, teacher, *teach_in_class):
        self.lesson = lesson
        self.teacher = teacher
        self.teach_in_class = teach_in_class


class School:
    list_students = []
    list_teacher = []
    list_class = []

    def add_student(self, study_in_class, name, mather, father):
        self.list_students.append(AddStudent(study_in_class, name, mather, father))

    def add_teacher(self, lesson, teacher, *teach_in_class):
        self.list_teacher.append(AddTeacher(lesson, teacher, *teach_in_class))
        pass

    def get_all_class(self):
        print('GET ALL CLASS IN SCHOOL')
        for students in self.list_students:
            if students.study_in_class not in self.list_class:
                self.list_class.append(students.study_in_class)

        for teacher in self.list_teacher:
            if teacher.teach_in_class not in self.list_class:
                for school_class in teacher.teach_in_class:
                    self.list_class.append(school_class)
        self.list_class = list(set(self.list_class))
        self.list_class.sort()
        for school_class in self.list_class:
            print(school_class)
        print()

    def get_all_student_in_class(self, school_class):
        print(f'GET ALL STUDENTS IN CLASS {school_class}')
        for students in self.list_students:
            if students.study_in_class == school_class:
                print(students.name)
        print()

    def get_all_lesson(self, student_name):
        print(f'GET ALL LESSON FOR {student_name}')
        for student in self.list_students:
            if student.name == student_name:
                students_class = student.study_in_class
        for teacher in self.list_teacher:
            if students_class in teacher.teach_in_class:
                print(teacher.lesson)
        print()

    def get_all_perents(self, name_student):
        print(f'GET ALL PERENTS {name_student}')
        for students in self.list_students:
            if students.name == name_student:
                print(students.name_mather)
                print(students.name_father)
        print()

    def get_all_teacher(self, school_class):
        print(f'Get All Teacher in {school_class}')
        for teacher in self.list_teacher:
            if school_class in teacher.teach_in_class:
                print(teacher.teacher)
        print()


school = School()
school.add_student('a1', 'ivanov s.s.', 'mama sveta', 'papa serega')
school.add_student('a1', 'petrov a.a.', 'mama ira', 'papa vadim')
school.add_student('a2', 'sidorov f.f.', 'mama lida', 'papa vanya')
school.add_student('b1', 'kozlov l.m.', 'mama marina', 'papa roma')
school.add_student('b1', 'borisov r.t.', 'mama masha', 'papa ilia')
school.add_student('b1', 'bobrov f.f.', 'mama galya', 'papa boris')
school.add_student('c1', 'vaflya r.r', 'mama olga', 'papa oleg')
school.add_student('c1', 'jigulo g.g', 'mama polina', 'papa maksim')

school.add_teacher('mathematics', 'Belikov', 'a1', 'a2')
school.add_teacher('english', 'Romanov', 'b1', 'b2')
school.add_teacher('physical', 'Surikov', 'a1', 'a2', 'b1', 'c1')
school.add_teacher('geography', 'Vodnikov', 'b1', 'c1')
school.add_teacher('painting', 'Suvorov', 'a1', 'c1', 'd1', 'd2')

school.get_all_class()
school.get_all_student_in_class('a1')
school.get_all_lesson('ivanov s.s.')
school.get_all_lesson('kozlov l.m.')
school.get_all_perents('kozlov l.m.')
school.get_all_teacher('b1')
school.get_all_teacher('a1')

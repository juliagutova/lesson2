'''
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter
def get_students():
    names =[]
    for name in students:   
        names.append(name['first_name'])
    pop_name = Counter(names).most_common()
    for nam in pop_name:
        print(f'{nam[0]}: {nam[1]}')
    return names

get_students()



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
from collections import Counter
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# Пример вывода:
# Самое частое имя среди учеников: Маша
students_numbers = []
for stud in students:
    stud_list = (stud['first_name'])
    students_numbers.append(stud_list)
name = Counter(students_numbers).most_common(1)
for n in name:
    print(f'Самое частое имя среди учеников: {n[0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
from collections import Counter
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

first_class = []
for stud in school_students:
    stud_list = (stud[0]['first_name'])
    first_class.append(stud_list)
names = Counter(first_class).most_common()
print(names)
for name in names:
    print(f'Самое частое имя в классе: {name[0]}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for school_class in school:
    boys = 0
    girls = 0
    for student in school_class['students']: 
        if is_male.get(student['first_name']) == False:
            girls += 1
        if is_male.get(student['first_name']) == True:
            boys += 1
    if girls + boys == len(school_class['students']):
        print(f'В классе {school_class["class"]}: {girls} девочки и {boys} мальчика')
        
 
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

'''
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for school_class in school:
    boys = 0
    girls = 0
    for student in school_class['students']: 
        if is_male.get(student['first_name']) == False:
            girls += 1
        if is_male.get(student['first_name']) == True:
            boys += 1
    if girls > boys:
        print(f'Больше всего девочек в классе {school_class["class"]}')
    else:
        print(f'Больше всего мальчиков в классе {school_class["class"]}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

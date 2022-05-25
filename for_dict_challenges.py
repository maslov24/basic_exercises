print('Задание 1')
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
for i in students:
    names.append(i['first_name'])
    #print(names)
test_names = ' '.join(names)
compare_quantity_names = {}
dict_students = {}
for name in names:
    if name in test_names:
        quantity_name = names.count(name)
        print(f'{name}: {quantity_name}')
        test_names=test_names.replace(name,'').strip()
        names=test_names.split()

print('Задание 2')
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
def max_quantity_names_1(students):
    names = []
    for i in students:
        names.append(i['first_name'])
        #print(names)
    test_names = ' '.join(names)
    compare_quantity_names = {}
    dict_students = {}
    for name in names:
        if name in test_names:
            quantity_name = names.count(name)
            print(f'{name}: {quantity_name}')
            test_names=test_names.replace(name,'').strip()
            names=test_names.split()
            dict_students[name]= quantity_name
    max_quantity_names = dict_students.values()
    max_quantity_names_key = max(dict_students, key=dict_students.get)
    return max_quantity_names_key

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

print(f'Самое частое имя среди учеников: {max_quantity_names_1(students)}')



print('Задание 3')
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

def max_quantity_names_2(students):
    names = []
    for i in students:
        names.append(i['first_name'])
    test_names = ' '.join(names)
    compare_quantity_names = {}
    dict_students = {}
    for name in names:
        if name in test_names:
            quantity_name = names.count(name)
            #print(f'{name}: {quantity_name}')
            test_names=test_names.replace(name,'').strip()
            names=test_names.split()
            dict_students[name]= quantity_name
    max_quantity_names = dict_students.values()
    max_quantity_names_key = max(dict_students, key=dict_students.get)
    return max_quantity_names_key

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
count = 0
for students in school_students:
    count += 1
    print(f'Самое частое имя в классе {count}: {max_quantity_names_2(students)}')


print('Задание 4')
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2г', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for class_school in school:
    girls_class = 0
    boys_class = 0
    for student_class_school in class_school['students']:
        if student_class_school['first_name'] in is_male:
            #girls_class += 1  if is_male[student_class_school['first_name']] == False else boys_class += 1
            if is_male[student_class_school['first_name']] == True:
                boys_class += 1
            else:
                girls_class += 1
    print (f'Класс {class_school["class"]}: девочки {girls_class}, мальчики {boys_class}')
    
  
print('Задание 5')
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
class_quantity_boys = {}
class_quantity_girls = {}
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
for class_school in school:
    girls_class = 0
    boys_class = 0
    for student_class_school in class_school['students']:
        if student_class_school['first_name'] in is_male:
            #girls_class += 1  if is_male[student_class_school['first_name']] == False else boys_class += 1
            if is_male[student_class_school['first_name']] == True:
                boys_class += 1
            else:
                girls_class += 1
    #print (f'Класс {class_school["class"]}: девочки {girls_class}, мальчики {boys_class}')
    class_quantity_boys[class_school["class"]] = boys_class
    class_quantity_girls[class_school["class"]] = girls_class

max_class_quantity_boys = max(class_quantity_boys, key=class_quantity_boys.get)
max_class_quantity_girls = max(class_quantity_girls, key=class_quantity_girls.get)

print('Больше всего мальчиков в классе', max_class_quantity_boys)
print('Больше всего девочек в классе', max_class_quantity_girls)   
 


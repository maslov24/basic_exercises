# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
pupil_name_line = ''
pupil_name_line2 = ', '
for pupil_name in names:
    print(pupil_name)
    pupil_name_line = pupil_name + ' ' + pupil_name_line 

print(pupil_name_line.strip().replace(' ', ', '))

print(pupil_name_line2.join(names))


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for pupil_name in names:
    print(f'{pupil_name}: {len(pupil_name)}')



# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    if is_male[name] == True:
        print(name, 'М')
    else:
        print(name, 'Ж')  


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего {len(groups)} группы.')
for number_group in range(len(groups)):
    print(f'Группа {number_group+1}: {len(groups[number_group])} ученика.')


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
for number_group in range(len(groups)):
    print(f'Гуппа {number_group + 1}: {", ".join(groups[number_group])}.')
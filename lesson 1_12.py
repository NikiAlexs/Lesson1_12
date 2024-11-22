#name = input("Введите ваше имя: ")
#current_year = 2024
#date_of_birth = int(input("В каком году вы родились? "))
#age = current_year - date_of_birth
#print("Здравствуйте,", name)
#print("В этом году вам ", age, "лет"+'.')
from itertools import count
from os import symlink

print('привет, я строка в нижнем регистре'.upper())     #lower
print('привет, я строка в нижнем регистре'.replace('привет','пока'))
print('привет, я строка в нижнем регистре'.replace(' ','!!!'))

#Практическое задание 1_4
my_string = (input("Введите ваши ФИО: "))
print("Количество символов: ", len(my_string))
print("Количество букв: ", len(my_string.replace(' ','')))
print('Верхний регистр: ',my_string.upper())
print('Нижний регистр: ',my_string.lower())
print('Без пробелов: ', my_string.replace(' ',''))
print(my_string[0])
print(my_string[-1])

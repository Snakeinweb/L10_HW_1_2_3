# a=int(input())
# str_a=str(a)
# s=len(str_a)
# print(str_a[s-1])

from typing import KeysView


b ="Вид питомца"
c ="Возраст питомца"
d ="Имя владельца"

pets={}

name_owner = input("Имя хозяина питомца: ")
name_pets = input("Как зовут питомца?: ")
who_pets = input("Кто ваш питомец?: ")
age_pets = int(input("Сколько лет питомцу?: "))

# Обработка правильного соответствия с указанным возрастом выводит год, годаили лет до 100

str_age_pets = str(age_pets)
s = len(str_age_pets)

s_last = int(str_age_pets[s-1])
if s_last == 2 and age_pets != 12:
    f_age = "года"
elif s_last == 3 and age_pets != 13:
    f_age = "года"
elif s_last == 4 and age_pets != 14:
    f_age = "года"
elif s_last == 1 and age_pets != 11:
    f_age = "год"
else:
    f_age = "лет"

# Обработка правильного соответствия с указанным возрастом выводит год, годаили лет больше 100
    
s_2_last = int(str_age_pets[s-2:])
if s_last == 2 and s_2_last != 12:
    f_age = "года"
elif s_last == 3 and s_2_last != 13:
    f_age = "года"
elif s_last == 4 and s_2_last != 14:
    f_age = "года"
elif s_last == 1 and s_2_last != 11:
    f_age = "год"
else:
    f_age = "лет"



pets = {
    name_pets : {
        b : who_pets,
        c : age_pets,
        d : name_owner
        }
        }

print ('Это', who_pets, 'по кличке', '"'+name_pets+'"'+'. Возраст:', age_pets, f_age)
print (pets)

print (f' Это {pets[name_pets][b]} по кличке {pets[name_pets]}. Возраст: {pets[name_pets][c]} {f_age}. Имя владельца: {pets[name_pets][d]}')

# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша

print (f' Это {pets[name_pets][b]} по кличке {pets[name_pets]}. Возраст: {pets[name_pets][c]} {f_age}. Имя владельца: {pets[name_pets][d]}')
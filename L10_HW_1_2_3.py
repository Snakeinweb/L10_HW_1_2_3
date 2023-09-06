# a=int(input())
# str_a=str(a)
# s=len(str_a)
# print(str_a[s-1])

b ="Вид питомца"
c ="Возраст питомца"
d ="Имя владельца"

pets={}

name_owner = input("Имя хозяина питомца: ")
name_pets = input("Как зовут питомца?: ")
who_pets = input("Кто ваш питомец?: ")
age_pets = int(input("Сколько лет питомцу?: "))

str_age_pets = str(age_pets)
s = len(str_age_pets)
s_last = int(str_age_pets[s-1])
if s_last == 2 or 3 or 4 and age_pets != 12 or 13 or 14:
    f_age = "года"
elif s_last == 1 and age_pets != 11:
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
print ("Это", who_pets, "по кличке", name_pets + ". Возраст:", age_pets, f_age)



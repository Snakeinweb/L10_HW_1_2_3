#

# print('Здравствуйте')

prif = 'лет'

who_animal = input('Кто ваш питомец? ')

name = input('Имя вашего питомца? ')

age = int(input('Возраст вашего питомца? '))

# в дальнейшем можно обработать до других "лет"

if age == 1:

    prif = 'год'

else:

    if age >= 2 and age <= 4:

        prif = 'года'

print('Это',who_animal,'по кличке "'+name+'". Возраст:',age,prif)

pets = {}
#n = int(input('Введите колличество питомцев вводимых в базу: '))
#for i in range(n):
name = input ("Введите кличку питомца: ")
pets[name] = 0


print (pets)



task = int(input('Запустить задачу номер: '))
if task == 1:
# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

    def person_info(name, age, city):
        result = f'{name}, {age} год(а), проживает в городе {city}'
        return result

    print(person_info('Василий', 21, 'Москва'))
    print(person_info('Дмитрий', 25, 'Санкт-Петербург'))

elif task == 2:
#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

    def max_numbers(a, b, c):
        result = max([a, b, c])
        return result

    print(max_numbers(2, 8, 19))

elif task == 3 or task == 4:
# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. 
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

    player_name = input('Введите имя игрока: ')
    player = {
        'name' : player_name,
        'health' : 100,
        'damage' : 50,
        'armor' : 1.2
        }

    enemy_name = input('Введите имя врага: ')
    enemy = {
        'name' : enemy_name,
        'health' : 50,
        'damage' : 30,
        'armor' : 1
    }

    def get_damage(damage, armor):
        return damage / armor

    def attak(unit, target):
        damage = get_damage(unit['damage'], target['armor'])
        target['health'] -= damage

    attak(player, enemy)
    print(enemy)

    attak(enemy, player)
    print(player)


import json

class Crudjson(object):
    file = None

    def __init__(self, file):
        self.file = file

    def create(self, data):
            with open (self.file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f'✅ Данные записаны в {self.file} успешно!')


    def add(self, new_data):
        with open(self.file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f'Данные из файла: {data}')
            data.update(new_data)
            print(f'Обновленные данные из файла: {data}')
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print(f'✅ Новые данные записаны в {self.file} успешно!')

    def delete(self, key):
        with open(self.file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            del data[key]
            print('Ключ удален!')
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print('✅ Файл готов!' )

if __name__ == '__main__':

    file = 'crud6.json'

    writer = Crudjson(file)

    dictionary = {
        'name': 'Sergey',
        'age': 25,
        'skills': ['python', 'sql', 'fifa2024']
    }

    writer.create(dictionary)

    new_data = {
        'city': 'Moscow',
        'hobby': 'football'
    }

    writer.add(new_data)

    writer.delete('hobby')

    print('ЕЛЕ СДЕЛАЛ...')





# with open('crud6.json', 'r', encoding='utf-8') as file:
#     text = file.read(50)
#     print(text)
#
#     position = file.tell()
#     print(position)
#     file.close()










#11111111111111111111111111111111111111111111111111111111111111111111111111

# class Cat(object):
#     name = None
#
#     def __init__(self, name):
#         self.name = name
#
#     def meow(self):
#         print(self.name, 'говорит: Мяу!')
#
#
# my_cat = Cat('Барсик').meow()
#
# my_cat.meow()
#
# 2222222222222222222222222222222222222222222222222222222222222222

# class Dog(object):
#     name = None
#     age = None
#
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def gavv(self):
#         print(f'{self.name} в {self.age} года говорит: Гав!')
#
# my_dog = Dog('Шарик', 33)
#
# my_dog.gavv()

# 33333333333333333333333333333333333333333333333333333333333

# class Zenit(object):
#
#     age = None
#     wins = None
#     players = None
#     name = None
#
#
#     def __init__(self, name, age, wins, players):
#         self.age = age
#         self.wins = wins
#         self.players = players
#         self.name = name
#
#     def play(self):
#         print(f"команда {self.name} существует с"
#               f" {self.age} года, имеет {self.wins}"
#               f" побед и {self.players} игроков")
#
# team = Zenit('Zenit', 1945, 999, 56 )
#
# team.play()

# 44444444444444444444444444444444444444444444444444444444444444444444444444444444444444

# class Sergo(object):
#     age = None
#     name = None
#     plays = None
#
#     def __init__(self, age, name, plays):
#         self.age = age
#         self.name = name
#         self.plays = plays
#
#     def my_life(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age} лет и я люблю играть в {self.plays}')
#
#
# if __name__ == '__main__':
#
#     life = Sergo(25, 'Сережа', 'футбол')
#
#     life.my_life()




























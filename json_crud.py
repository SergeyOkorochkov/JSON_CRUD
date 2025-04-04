import logging
import json

# Настраиваем логирование
logging.basicConfig(
    level=logging.DEBUG,
    filename='log_json_py.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Crudjson(object):
    file = None
    logging.info(f'Класс успешно создан')

    def __init__(self, file):
        self.file = file

    def create(self, data):
        try:
            with open (self.file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            logging.info(f'✅ Данные записаны в {self.file} успешно!')
        except Exception as e: #почему и зачем "as e"????????????????????
            logging.exception(f'Не удалось открыть/создать файл {self.file}')


    def add(self, new_data):
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                logging.info(f'Данные из файла {self.file}: {data}')
                data.update(new_data)
                logging.info(f'Успешно добавлены данные в файл: {self.file}')
            with open(self.file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                logging.info(f'✅ Новые данные записаны в {self.file} успешно!')
        except Exception as e:
            logging.exception(f'Не удалось добавить новые данные в файл {self.file}')

    def delete(self, key):
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if key in data:
                    del data[key]
                    logging.info(f'Ключ {key} удален!')
                else:
                    logging.warning(f'Ключ {key} не найден')
            with open(self.file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                logging.info(f'✅ Файл {self.file} готов, данные загружены!')
        except Exception as e:
            logging.exception(f'Ошибка при удалении ключа {key}')

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








# import logging
#
# # Если хочу дописывать, нужно поставить 'a'.
# logging.basicConfig(level=logging.DEBUG,
#                     filename='log_json_py.log',
#                     filemode='w',
#                     format='%(asctime)s %(levelname)s %(message)s')
#
# logging.debug('A DEBUG Message')
# logging.info('AN INFO')
# logging.warning('A WARNING')
# logging.error('AN ERROR')
# logging.critical('A message of CRITICAL severity')
#
# x_vals = [3, 5, 9, 7]
# y_vals = [3, 8, 0, 2]
#
# for x_val, y_val in zip (x_vals, y_vals):
#     x, y = x_val, y_val
#     logging.info(f'The values of {x} and {y}.')
#     try:
#         a = x/y
#         logging.info(f'x/y successful with result: {a}.')
#     except ZeroDivisionError as err:
#        # logging.error("ZeroDIVISIONERROR", exc_info=True)
#         logging.exception('ZeroDivisionError')
#
#











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
# my_cat = Cat('Барсик')
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




























#Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
#расширение
#минимальная длина случайно сгенерированного имени, по умолчанию 6
#максимальная длина случайно сгенерированного имени, по умолчанию 30
#минимальное число случайных байт, записанных в файл, по умолчанию 256
#максимальное число случайных байт, записанных в файл, по умолчанию 4096
#количество файлов, по умолчанию 42
#? мя файла и его размер должны быть в рамках переданного диапазона.
#21:48
#Задание №5
#✔ Доработаем предыдущую задачу.
#✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
#✔ Расширения и количество файлов функция принимает в качестве параметров.
#✔ Количество переданных расширений может быть любым.
#✔ Количество файлов для каждого расширения различно.
#✔ Внутри используйте вызов функции из прошлой задачи

import random
from random import randint

MIN_LEN_NAME = 6
MAX_LEN_NAME = 30
MIN_SIZE = 256
MAX_SIZE = 4096
COUNT_FILE = 42
STR_CHAR = 'qwrtpsdfghjklzxcvbnmeyuioa'
def create_file(exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE, max_size=MAX_SIZE,
                count_file=COUNT_FILE ):
    for _ in range(0, count_file):
        name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp

        with open(name_file, 'wb') as f:
            f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))
def input_exp():
    exp_count = int(input("Введите кол-во расширений файлов : "))
    exp=[]
    count_file = set()
    dict_exp={}
    [exp.append(input('Введите обозначение расширения : ')) for i in range(exp_count) ]
    while (len(count_file) < len(exp)):
            [ count_file.add(randint(1, 5)) for i in range(exp_count)  if count_file not in count_file ]
    for i in range(exp_count):
        dict_exp=dict(zip(exp,list(count_file)))
    print(exp)
    print(count_file)
    print(dict_exp)
    return dict_exp
def gen_files(input_exp :dict):

    for key, value in input_exp().items():
        create_file(key, count_file=value)

if __name__ == '__main__':

    gen_files(input_exp)

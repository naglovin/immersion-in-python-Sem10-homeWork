# Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.


from random import randint
from random import uniform # Функция uniform () определена в модуле random стандартной библиотеки Python. Он возвращает случайное число с плавающей запятой между заданным диапазоном чисел.

class Create_File_Numbers:

    __min = -1000
    __max = 1000

    def __init__(self, count: int, name: str):
        self.count = count
        self.name = name

    def numbers_file(self):
        with open(self.name, 'w', encoding='utf-8') as f:
            for i in range(self.count):
                temp_res = f'{randint(self.__min, self.__max)}|{uniform(self.__min, self.__max)}'
                f.write(f"{temp_res}\n")

class Generate_File_Names:

    __min = 4
    __max = 8

    def __init__(self, count: int, names: str):
        self.count = count
        self.names = names

    def generate_names(self):
        vowels = "aeiouy"
        consonants = "qwrtpsdfghjklzxcvbnm"
        with open(self.names, 'w', encoding='utf-8') as f:
            for i in range(self.count):
                name = ""
                for i in range(randint(self.__min, self.__max)//2):
                    name += (vowels[randint(0, len(vowels)-1)])
                    name += (consonants[randint(0, len(consonants)-1)])
                name = name.capitalize()
                f.write(f"{name}\n")

test1 = Create_File_Numbers(7, "test.txt")
test1.numbers_file()
print(test1.name)

test2 = Generate_File_Names(5, "names.txt")
test2.generate_names()
print(test2.names)
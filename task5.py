# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.


class Animals:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def name_animal(self):
        return self.name


class Fish(Animals):
    def __init__(self, fresh_water, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fresh_water = fresh_water
        self.deep = deep

    def specific(self):
        if self.fresh_water:
            return True
        return False

    def check_deep(self):
        if self.deep <= 3:
            return f"Мелководное до {self.deep} метров"
        elif 3 < self.deep < 20:
            return f"Среднеглубинное до {self.deep} метров"
        return f"Глубоководное глубже {self.deep} метров"

class Birds(Animals):

    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        wing_lengh = self.wingspan * 0, 45
        return wing_lengh


class Elephant(Animals):

    def __init__(self, tusk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tusk = tusk

    def specific(self):
        if self.tusk:
            return True
        return False


elephant = Elephant(False, 'Слон', True)
print(f"Название: {elephant.name}, Хобот: {elephant.tail}, Бивень: {elephant.tusk}")

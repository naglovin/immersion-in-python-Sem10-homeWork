# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.



from task5 import Fish, Birds, Elephant


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"птичка": Birds, "слоник": Elephant, "рыбка": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    #animal_from_fabric = fabric.make_animal("Слон", "Кузя", "пятнистый")
    #print(animal_from_fabric)
    print(fabric)
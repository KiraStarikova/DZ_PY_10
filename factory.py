# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа
# и верните его из класса-фабрики.

class Animals:

    def __init__(self, name: str, age: int, say: str, eat: str):
        self.name = name
        self.age = age
        self.say = say
        self.eat = eat



    def say(self):
        pass

    def eat(self):
        return " делаю ням-ням"

    def __str__(self):
        return f"{self.name} {self.age} {self.say} {self.eat}"



class Fish(Animals):

    def __init__(self, name: str, age: int, say: str, eat: str):
        super().__init__(name, age, say, eat)

    def say(self):
        return ("кар-кар")

    def eat(self):
        return ("ням-ням")

    def __str__(self):
        return f"{super().__str__()}"



class Birds(Animals):

    def __init__(self, name: str, age: int,  say: str, eat: str):

        super().__init__(name, age, say, eat)

    def say(self):
        return ("чик-чирик")

    def eat(self):
        return ("ням-ням")

    def __str__(self):
        return f"{super().__str__()} "


if __name__ == '__main__':
    fish1 = Fish("karl", 2, "говорю буль-буль", " делаю ням-ням")
    bird1 = Birds("Chig", 2, "говорю кар-кар", "делаю ням-ням")
    print(fish1)
    print(bird1)


from factory import Animals, Fish, Birds


class Factory(Birds, Fish, Animals):

    @staticmethod
    def create_animal(name: str, age: int, say: str, eat: str):
        return Animals(name, age, say, eat)

    @staticmethod
    def create_fish(name: str, age: int, say: str, eat: str):
        return Fish(name, age, say, eat)

    @staticmethod
    def create_bird(name: str, age: int,  say: str, eat: str):
        return Birds(name, age, say, eat)


if __name__ == '__main__':
    any_animal = Factory.create_animal('Monster', 999, 'grrrrrrrrr', 'hriam-hriam')
    print(any_animal)
    raven = Factory.create_bird('Raven', 99, 'kra - kra', 'am - am')
    print(raven)
    shark = Factory.create_fish('Aculina', 67, ' bul- bul', 'niam - niam')
    print(shark)

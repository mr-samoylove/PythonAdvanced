import Animal


class Mammal(Animal.Animal):
    def __init__(self, name='No name', age='Unknown', amount_of_legs='Unknown'):
        super().__init__(name, age)
        self.__amount_of_legs = amount_of_legs

    def say(self):
        print("Я млекопитающее")

import Animal


class Fish(Animal.Animal):
    def __init__(self, name='No name', age='Unknown', species_type='Unknown'):
        super().__init__(name, age)
        self.__type = species_type

    def say(self):
        print("Бульк")

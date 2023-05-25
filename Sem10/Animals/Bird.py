import Animal


class Bird(Animal.Animal):
    def __init__(self, name='No name', age='Unknown', max_height='Unknown'):
        super().__init__(name, age)
        self.__max_height = max_height

    def say(self):
        print("То ли чик-чирик, то ли курлык")

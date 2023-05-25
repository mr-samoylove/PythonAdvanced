class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def how_old(self):
        return self.__age

    def whats_the_name(self):
        return self.name
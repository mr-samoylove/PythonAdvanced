class Factory:
    def make_animal(self, typename, *args, **kwargs):
        try:
            return typename(*args, **kwargs)
        except RuntimeError as e:
            print(e)
            return None


if __name__ == '__main__':
    from Sem_10.Animals.Fish import Fish

    factory = Factory()
    new_fish = factory.make_animal(typename=Fish, name='Dora')
    if new_fish:
        new_fish.say()

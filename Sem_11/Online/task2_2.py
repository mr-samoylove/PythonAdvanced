class Archive:
    """
    Архив, который хранит пару свойств. Например, число и строку.
    При создании нового экземпляра класса,
    старые данные из ранее созданных экземпляров сохраняются в пару списков архивов.
    list-архивы также являются свойствами экземпляра.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Actually a Singleton patten lol
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.all_previous_numbers = list()
            cls._instance.all_previous_strings = list()
        else:
            cls._instance.all_previous_numbers.append(cls._instance.number)
            cls._instance.all_previous_strings.append(cls._instance.some_str)
        return cls._instance

    def __init__(self, number, some_str):
        """
        init
        :param number: int
        :param some_str: str
        """
        self.number = number
        self.some_str = some_str

    def __str__(self):
        """
        Human-readable representation
        :return:
        """
        return f'Number: {self.number} ||| string: {self.some_str} ||| ' \
               f'archive: {list(zip(self.all_previous_numbers, self.all_previous_strings))}'

    def __repr__(self):
        return f'Archive({self.number}, "{self.some_str}")'


if __name__ == '__main__':
    # arc1 = Archive(1, "str1")
    # print(arc1)
    # arc2 = Archive(2, "str2")
    # print(arc2)
    # arc3 = Archive(3, "str3")
    # print(arc3)

    arc4 = Archive(3, "str3")
    print(arc4.__repr__())


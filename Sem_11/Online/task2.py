class Archive:
    all_previous_numbers = list()
    all_previous_strings = list()
    last_number = None
    last_str = None

    def __init__(self, number, some_str):
        self.number = number
        self.some_str = some_str

        if Archive.last_number is not None:
            Archive.all_previous_numbers.append(Archive.last_number)
            Archive.all_previous_strings.append(Archive.last_str)

        Archive.last_number = number
        Archive.last_str = some_str

    def __str__(self):
        return f'Number: {self.number} ||| string: {self.some_str} ||| ' \
               f'archive: {list(zip(Archive.all_previous_numbers, Archive.all_previous_strings))}'


if __name__ == '__main__':
    arc1 = Archive(1, "str1")
    print(arc1)
    arc2 = Archive(2, "str2")
    print(arc2)
    arc3 = Archive(3, "str3")
    print(arc3)
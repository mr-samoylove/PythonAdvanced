import datetime


class MyStr(str):
    """
    My class
    """
    def __new__(cls, value, author_name):
        """
        Some text lol,
        :param value: str
        :param author_name: str
        creation_time is datetime.now()
        """
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.creation_time = datetime.datetime.now()
        return instance




if __name__ == '__main__':
    s = MyStr("stroka", "Ilyusha")
    print(s, s.author_name, s.creation_time)
    print(s.upper())

    print(help(MyStr))

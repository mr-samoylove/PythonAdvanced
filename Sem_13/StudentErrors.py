class UsernameTypeError(TypeError):
    def __init__(self, wrong_name):
        self.wrong_name = wrong_name

    def __str__(self):
        return f'Имя и Фамилия должны быть строками, а вы ввели имя {self.wrong_name} типа {type(self.wrong_name)}'


class UsernameValueError(ValueError):
    def __init__(self, wrong_name):
        self.wrong_name = wrong_name

    def __str__(self):
        return f'Имя и Фамилия должны состоять только из букв и начинаться с заглавной буквы, а вы ввели {self.wrong_name}'


class GradesTypeError(TypeError):
    def __init__(self, wrong_grade):
        self.wrong_grade = wrong_grade

    def __str__(self):
        return f'Оценка должна быть целым числом, а вы ввели {type(self.wrong_grade)}'


class GradesOutOfBound(ValueError):
    def __init__(self, wrong_grade, lower_bound, upper_bound):
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.wrong_grade = wrong_grade

    def __str__(self):
        return f'Данная оценка может быть от {self.lower_bound} до {self.upper_bound}, а вы ввели {self.wrong_grade}'

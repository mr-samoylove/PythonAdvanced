import csv


class StudentDescriptor:
    SEMINARS_MIN_GRADE = 2
    SEMINARS_MAX_GRADE = 5
    EXAM_MIN_GRADE = 0
    EXAM_MAX_GRADE = 100

    def __init__(self, mode: str = None):
        self.mode = mode

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        match self.mode.lower():
            case 'name':
                self.validate_name(value)
            case _:
                raise RuntimeWarning(f"В StudentDescriptor был передан несуществующий режим работы {self.mode}")
        setattr(instance, self.param_name, value)

    def validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'Имя и Фамилия должны быть строками, а вы ввели {type(name)}')
        if not name.isalpha() or not name.istitle():
            raise ValueError(f'Имя и Фамилия должны состоять только из букв и начинаться с заглавной буквы, '
                             f'а вы ввели {name}')

    @staticmethod
    def validate_seminars_grades(grade):
        if not isinstance(grade, int):
            raise TypeError(f'Оценка должна быть целым числом, а вы ввели {type(grade)}')
        if not StudentDescriptor.SEMINARS_MIN_GRADE <= grade <= StudentDescriptor.SEMINARS_MAX_GRADE:
            raise ValueError(f'Оценка семинаров может быть от {StudentDescriptor.SEMINARS_MIN_GRADE}'
                             f' до {StudentDescriptor.SEMINARS_MAX_GRADE},'
                             f' а вы ввели {grade}')

    @staticmethod
    def validate_exam_grades(grade):
        if not isinstance(grade, int):
            raise TypeError(f'Оценка должна быть целым числом, а вы ввели {type(grade)}')
        if not StudentDescriptor.EXAM_MIN_GRADE <= grade <= StudentDescriptor.EXAM_MAX_GRADE:
            raise ValueError(f'Оценка экзаменов может быть от {StudentDescriptor.EXAM_MIN_GRADE}'
                             f' до {StudentDescriptor.EXAM_MAX_GRADE},'
                             f' а вы ввели {grade}')


class Student:
    first_name = StudentDescriptor(mode='name')
    last_name = StudentDescriptor(mode='name')

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        with open("classes_names.csv", 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            self.__slots__ = ("first_name", "last_name", *(line[0] for line in reader))
            for course in self.__slots__[2:]:
                setattr(Student, course, dict(seminars=list(), exams=list()))

    def __str__(self):
        return f"Студент {self.first_name} {self.last_name}.\n" \
               f"Его оценки:\n" + \
               '\n'.join(f'{course} = {self.__getattribute__(course)}' for course in self.__slots__[2:])

    def set_grade(self, course: str, type_of_lesson: str, grade: int):
        if course not in self.__slots__:
            raise KeyError(f"Студент {self.first_name} {self.last_name} не изучает предмет {course}")
        match type_of_lesson.lower():
            case "seminar":
                StudentDescriptor.validate_seminars_grades(grade)
                self.__getattribute__(course)["seminars"].append(grade)
            case "exam":
                StudentDescriptor.validate_exam_grades(grade)
                self.__getattribute__(course)["exams"].append(grade)
            case _:
                raise RuntimeError("Вы поставили оценку по несуществующему типу занятий")

    def print_avg_exams(self):
        avgs = {
            course: sum(self.__getattribute__(course)["exams"]) / len(self.__getattribute__(course)["exams"])
            if len(self.__getattribute__(course)["exams"]) != 0 else None
            for course in self.__slots__[2:]
        }
        all_exam_grades = tuple(value
                                for value in avgs.values()
                                if value is not None)

        total = sum(all_exam_grades) / len(all_exam_grades) if len(all_exam_grades) != 0 else 0
        print(f"Средняя оценка всех экзаменов: {total},\n"
              f"Оценки по каждому предмету: {avgs}")


if __name__ == '__main__':
    # раскомментировать для генерации csv файла
    # import csv
    # with open("classes_names.csv", 'w', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows((('math',), ('philosophy',), ('PE',), ('computer science',)))

    # успешный кейс:
    oleg = Student("Oleg", "Ivanov")
    oleg.set_grade("math", "seminar", 4)
    oleg.set_grade("math", "seminar", 4)
    oleg.set_grade("math", "seminar", 5)
    oleg.set_grade("math", "exam", 100)
    oleg.set_grade("philosophy", "exam", 60)

    oleg.print_avg_exams()
    print(oleg)

    # несуществующая дисциплина
    # oleg.set_grade("sleep", "seminar", 3)

    # неверная оценка семинаров
    # oleg.set_grade("math", "seminar", 0)
    # oleg.set_grade("math", "seminar", 7)

    # неверная оценка экзаменов
    # oleg.set_grade("math", "exam", 101)
    # oleg.set_grade("math", "exam", 70.5)

    # несуществующий тип урока
    # oleg.set_grade("math", "webinar", 4)

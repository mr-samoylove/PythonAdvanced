# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os.path


def path_split(fullpath: str) -> tuple:
    path, fullname = fullpath.rsplit(os.path.sep, 1)
    name, extension = fullname.split('.')
    return path, name, extension


print(path_split(r"C:\Users\mrsam\Desktop\Other\Резюме.pdf"))

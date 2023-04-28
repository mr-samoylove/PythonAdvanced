def whatever():
    with (open('my_file', 'r', encoding='utf-8') as fnumbers,
          open('names.txt', 'r', encoding='utf-8') as fnames):
        numbers = fnumbers.readlines()
        names = fnames.readlines()

    lines_to_write = []
    length_of_longest = max(len(numbers), len(names))
    for i in range(length_of_longest):
        two_numbers = numbers[i % len(numbers)]
        a, b = map(float, two_numbers.split('|'))
        mult = a * b

        name = names[i % len(names)]
        if mult >= 0:
            lines_to_write.append(f'{name.upper().rstrip()}; {round(mult)}\n')
        else:
            lines_to_write.append(f'{name.lower().rstrip()}; {abs(mult)}\n')

    with open('endfile.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines_to_write)


whatever()
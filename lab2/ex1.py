import csv


def esc(code):
    return f'\u001b[{code}m'


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = st * (8 - i) + st
            if i == 9:
                array_in[i][j] = j
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for j in range(10):
            if abs(array_fi[i][0] - res[9 - j]) < st:
                for k in range(9):
                    if 8 - k == j:
                        array_fi[i][k + 1] = 1
    return array_fi


def draw_plot(array_pl):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + '\t' + str(int(array_pl[i][j])) + '\t'
            if array_pl[i][j] == 0:
                line += '  '
            if array_pl[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '\t0\t1 2 3 4 5 6 7 8 9 ' + END)


RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
BLACK = esc(40)
END = esc(0)

array_plot = [[0 for x in range(10)] for y in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 2
step = round(abs(result[0] - result[9]) / 9, 1)
print("Шаг: " + str(step) + "; Функция: y = x^2")


array_init(array_plot, step)
array_fill(array_plot, result, step)


draw_plot(array_plot)


def flag_fr():
    for i in range(6):
        print(f'{BLUE}{"  " * 4}{WHITE}{"  " * 4}{RED}{"  " * 4}{END}')


def design(kol=1):
    for i in range(3):
        line = ''
        for ii in range(kol):
            if i % 2 == 0:
                if ii % 2 == 0:
                    line += f'{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "}{END}'
                else:
                    line += f'{WHITE}{"  "}{BLACK}{"  "}{WHITE}{"  "}{END}'
            else:
                if ii % 2 == 0:
                    line += f'{WHITE}{"  "}{BLACK}{"  "}{WHITE}{"  "}{END}'
                else:
                    line += f'{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "}{END}'
        print(line)


def design2(kol=1):
    for i in range(3):
        line = ''
        for ii in range(kol):
            if i % 2 == 0:
                line += f'{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "}{END}'
            else:
                line += f'{WHITE}{"  "}{BLACK}{"  "}{WHITE}{"  "}{END}'
        print(line)


def get_books_info():
    with open('books.csv', 'r') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        next(table)
        before = 0
        after = 0

        for row in table:
            if int((row[6].split(' ')[0]).split("-")[0]) <= 2014:
                before += 1
            else:
                after += 1
        before_percent = before / (after+before)
        before_str = str(before_percent * 100).split(".")[0] + "%) "
        after_str = str(100 - int(str(before_percent * 100).split(".")[0])) + "%) "

    total_symbols = 50
    before_symbols = round(total_symbols * before_percent)
    after_symbols = total_symbols - before_symbols

    chart = f'{RED}{" " * before_symbols}{BLUE}{" " * after_symbols}{END}'

    print("Процентное соотношение книг до 2014 года и после: \n")
    print(chart)
    print(" ")
    print(f'{RED}{" "}{END}{" - Книги до 2014 года (включительно) (" + str(before_str)}{BLUE}{" "}{END}'
          f'{" - Книги после 2014 года (" + after_str}{END}')

    with open('books-en.csv', 'r') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        next(table)
        before = 0
        after = 0

        for row in table:
            if int(row[3]) <= 1980:
                before += 1
            else:
                after += 1
        before_percent = before / (after+before)
        before_str = str(before_percent * 100).split(".")[0] + "%) "
        after_str = str(100 - int(str(before_percent * 100).split(".")[0])) + "%) "

    total_symbols = 50
    before_symbols = round(total_symbols * before_percent)
    after_symbols = total_symbols - before_symbols

    chart = f'{RED}{" " * before_symbols}{BLUE}{" " * after_symbols}{END}'
    print(" ")
    print("Процентное соотношение книг до 1980 года и после: \n")
    print(chart)
    print(" ")
    print(f'{RED}{" "}{END}{" - Книги до 1980 года (включительно) (" + str(before_str)}{BLUE}{" "}{END}'
          f'{" - Книги после 1980 года (" + after_str}{END}')

print(" ")
print("Флаг Франции: ")
flag_fr()
print(" ")
print("Узор вариант 1: ")
design(1)
print(" ")
print("Узор вариант 2: ")
design2(1)
print(" ")
get_books_info()

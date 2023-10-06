import csv

author = input("Введите имя автора: ")
variant = int(input("Выберите вариант ограничения (от 1 до 10): "))
f = open('result.txt', 'w')

with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')

    headers = next(table)
    results = []

    restrictions = {
        1: lambda row: int(row[7].split(',')[0]) <= 150,  # До 150 рублей
        2: lambda row: int((row[6].split(' ')[0]).split("-")[-1]) <= 2016,  # До 2016 года
        3: lambda row: int((row[6].split(' ')[0]).split("-")[-1]) in [2014, 2016, 2017],  # Только 2014, 2016 и 2017 года
        4: lambda row: int(row[7].split(',')[0]) <= 200,  # До 200 рублей
        5: lambda row: True,  # Нет
        6: lambda row: int(row[7].split(',')[0]) >= 150,  # От 150 рублей
        7: lambda row: int((row[6].split(' ')[0]).split("-")[-1]) >= 2016 and int((row[6].split(' ')[0]).split("-")[-1]) <= 2018,  # От 2016 до 2018 года
        8: lambda row: int((row[6].split(' ')[0]).split("-")[-1]) in [2015, 2018],  # Только 2015 и 2018 года
        9: lambda row: int(row[7].split(',')[0]) >= 200,  # От 200 рублей
        10: lambda row: int((row[6].split(' ')[0]).split("-")[-1]) >= 2018  # От 2018 года
    }

    for row in table:
        if len(row) >= 4 and author in row[3]:
            print(row)
            if restrictions[variant](row):
                results.append(row)

    if len(results) == 0:
        print(f'Нет результатов для автора "{author}"')
    else:
        f.write('Результаты поиска по автору ' + author + 'с учетом выбранного ограничения (вариант'+ str(variant) +'):\n\n')
        for result in results:
            f.write(' '.join(map(str, result)) + "\n")
f.close()
import csv

f = open('result.txt','w')
f2 = open('result-en.txt', 'w')

with open('books.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')

    headers = next(table)

    sorted_rows = sorted(table, key=lambda row: float(row[8]), reverse=True)

    top_20_rows = sorted_rows[:20]


if len(top_20_rows) == 0:
        print('Нет результатов')
else:
    for res in top_20_rows:
        f.write(str(res) + "\n")
f.close()


with open('books-en.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')

    headers = next(table)

    sorted_rows = sorted(table, key=lambda row: float(row[5]), reverse=True)

    top_20_rows = sorted_rows[:20]


if len(top_20_rows) == 0:
        print('Нет результатов')
else:
    for res in top_20_rows:
        f2.write(str(res) + "\n")
f2.close()
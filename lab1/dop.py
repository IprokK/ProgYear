import csv

f = open('result.txt','w')
f2 = open('result-en.txt', 'w')

with open('books.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')

    headers = next(table)
    results = set()

    for row in table:
        res_str = row[12]
        res_list = res_str.split('#')

        for res in res_list:
            res = res.strip()
            if res:
                results.add(res)

if len(results) == 0:
        print('Нет результатов')
else:
    for res in results:
        f.write(str(res) + "\n")
f.close()


with open('books-en.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')

    headers = next(table)
    results = set()

    for row in table:
        res_str = row[4]
        results.add(res_str)

if len(results) == 0:
        print('Нет результатов')
else:
    for res in results:
        f2.write(str(res) + "\n")
f2.close()
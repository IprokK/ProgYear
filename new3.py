import csv
import random

f = open('result.txt','w')

with open('books.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')

    headers = next(table)
    results = []

    for row in table:
        results.append(row)

    selected_books = random.sample(results, 20)

    for index, book in enumerate(selected_books, start=1):
        author = book[4]
        title = book[1]
        year = str(int((book[6].split(' ')[0]).split(".")[-1]))
        bibliography = f"{author}. {title} - {year}\n"
        f.write(f"{index}. {bibliography}")

f.close()
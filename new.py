import csv
stramount = 0
nameamount = 0
with open('books.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    for row in table:
        if stramount !=0:
            if len(row[1]) > 30:
                nameamount +=1
        stramount += 1


print("Количество записей в файле books.csv: " + str(stramount-1))
print("Количество записей, у которых в поле 'Название' строка длиннее 30 символов: " + str(nameamount))

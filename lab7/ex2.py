import csv
import matplotlib.pyplot as plt
import numpy as np

x_array = np.zeros(3774)
y1_array = np.zeros(3774)
y2_array = np.zeros(3774)

with open('data1.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    headers = next(table)
    i = 0
    for row in table:
        if i == 0:
            print(row)
        x_array[i] = float(row[0])
        y1_array[i] = float(row[4])
        y2_array[i] = float(row[5])
        i += 1

plt.figure(figsize=(8, 6))

plt.plot(x_array, y1_array, label='1 от 4', color='red')

plt.plot(x_array, y2_array, label='1 от 5', color='blue')

plt.title('Зависимость оборотов двигателя и холостого хода от времени с момента запуска')
plt.xlabel('Время, (с)')
plt.ylabel('Обороты двигателя, (об/мин)')
plt.legend()

correlation = np.corrcoef(y1_array, y2_array)[0, 1]
plt.figure(figsize=(6, 5))
plt.scatter(y1_array, y2_array, color='green', label=f'Корреляция: {correlation:.2f}')
plt.title('График корреляции')

plt.show()

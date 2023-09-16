def knapsack(C, weight, cost, n):
    K = [[0 for x in range(C + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(C + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i - 1] <= j:
                K[i][j] = max(cost[i - 1] + K[i - 1][j - weight[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    return K


items = ['rifle', 'pistol', 'ammo', 'medkit', 'inhaler', 'knife',
        'axe', 'talisman', 'flask', 'antidote', 'food', 'crossbow']

designations = {'rifle': 'в', 'pistol': 'п', 'ammo': 'б', 'medkit': 'а', 'inhaler': 'и', 'knife': 'н', 'axe': 'т',
                'talisman': 'о', 'flask': 'ф', 'antidote': 'д', 'food': 'к', 'crossbow': 'р'}

values = [25, 15, 15, 20, 5, 15, 20, 25, 15, 10, 20, 20]
weights = [3, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2]
capacity = 8
all_points = sum(values)
init_points = 15
count = len(values)

K = knapsack(capacity, weights, values, count)
result = {}
td_array = []
i, j, total = count, capacity, 0
res = K[count][capacity]
while i > 0 and res > 0:
    if res != K[i - 1][j]:
        result[items[i-1]] = weights[i-1]
        total += weights[i - 1]
        res -= values[i - 1]
        j -= weights[i - 1]
    i -= 1

points = K[count][capacity] + init_points - (all_points - K[count][capacity])

for i in result:
    for ii in range(result[i]):
        ar = [designations[i]]
        td_array.append(ar)

columns = 2

for i in range(0, len(td_array), columns):
    row = td_array[i:i+columns]
    formatted_row = ','.join([f"[{item[0]}]" for item in row])
    print(formatted_row)

print('\nИтоговые очки выживания: ' + str(points))

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

def find_combinations(C, weight, values, items, index, current_combination, result):
    if C == 0:
        total_value = sum(values[i] for i in current_combination)
        points = total_value + init_points - (all_points - total_value)
        if points > 0:
            result.append(current_combination.copy())
        return
    if index == len(weight) or C < 0:
        return

    current_combination.append(index)
    find_combinations(C - weight[index], weight, values, items, index + 1, current_combination, result)
    current_combination.pop()
    find_combinations(C, weight, values, items, index + 1, current_combination, result)

items = ['rifle', 'pistol', 'ammo', 'medkit', 'inhaler', 'knife',
        'axe', 'talisman', 'flask', 'antidote', 'food', 'crossbow']

values = [25, 15, 15, 20, 5, 15, 20, 25, 15, 10, 20, 20]
weights = [3, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2]
capacity = 8
all_points = sum(values)
init_points = 15
count = len(values)

result = []
find_combinations(capacity, weights, values, items, 0, [], result)

for combination in result:
    print("Combination:", [items[i] for i in combination])
    total_weight = sum(weights[i] for i in combination)
    total_value = sum(values[i] for i in combination)
    points = total_value + init_points - (all_points - total_value)
    print("Total Weight:", total_weight)
    print("Total Value:", total_value)
    print("Points:", points)
    print()

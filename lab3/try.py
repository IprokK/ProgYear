# Заданные предметы и их характеристики
items = [
    {"name": "Rifle", "symbol": "R", "size": (3, 1), "points": 25},
    {"name": "Pistol", "symbol": "P", "size": (2, 1), "points": 15},
    {"name": "Ammo Pack", "symbol": "A", "size": (2, 1), "points": 15},
    {"name": "First Aid Kit", "symbol": "F", "size": (2, 1), "points": 20},
    {"name": "Inhaler", "symbol": "I", "size": (1, 1), "points": 5},
    {"name": "Knife", "symbol": "K", "size": (1, 1), "points": 15},
    {"name": "Axe", "symbol": "X", "size": (3, 1), "points": 20},
    {"name": "Amulet", "symbol": "M", "size": (1, 1), "points": 25},
    {"name": "Flask", "symbol": "L", "size": (1, 1), "points": 15},
    {"name": "Antidote", "symbol": "D", "size": (1, 1), "points": 10},
    {"name": "Food", "symbol": "E", "size": (2, 1), "points": 20},
    {"name": "Crossbow", "symbol": "C", "size": (2, 1), "points": 20}
]

# Размер рюкзака
backpack_size = (2, 4)

# Очки выживания Тома перед выбором предметов
initial_points = 15

def print_knapsack_solution(items, designations, values, weights, capacity, K):
    n = len(items)
    i, j = n, capacity
    result = [[' ' for _ in range(capacity + 1)] for _ in range(n + 1)]

    while i > 0 and K[i][j] > 0:
        if K[i][j] != K[i - 1][j]:
            item = designations[items[i - 1]]
            result[i][j] = item
            j -= weights[i - 1]
        i -= 1

    for row in result[1:]:
        print("[" + "],[".join(row[1:]) + "]")

# Функция для выбора предметов для рюкзака
def choose_items(items, backpack_size, initial_points):
    # Сортируем предметы по убыванию их ценности (очков)
    items = sorted(items, key=lambda x: x["points"], reverse=True)

    # Инициализируем матрицу для рюкзака размером (backpack_size[0] + 1) x (backpack_size[1] + 1)
    matrix = [[0] * (backpack_size[1] + 1) for _ in range(backpack_size[0] + 1)]

    # Инициализируем матрицу для хранения выбранных предметов
    selected_items = [[""] * (backpack_size[1] + 1) for _ in range(backpack_size[0] + 1)]

    for item in items:
        for i in range(backpack_size[0], 0, -1):
            for j in range(backpack_size[1], 0, -1):
                item_size = item["size"]
                if item_size[0] <= i and item_size[1] <= j:
                    if matrix[i][j] < matrix[i - item_size[0]][j - item_size[1]] + item["points"]:
                        matrix[i][j] = matrix[i - item_size[0]][j - item_size[1]] + item["points"]
                        selected_items[i][j] = item["symbol"]

    # Восстанавливаем выбранные предметы
    i, j = backpack_size[0], backpack_size[1]
    selected = []
    while i > 0 and j > 0:
        item_symbol = selected_items[i][j]
        if item_symbol:
            selected.append(item_symbol)
            item_size = next(item["size"] for item in items if item["symbol"] == item_symbol)
            i -= item_size[0]
            j -= item_size[1]
        else:
            break

    # Проверяем, есть ли необходимые предметы для астмы и заражения
    if "I" not in selected:
        selected.append("I")  # Добавляем ингалятор, если его нет
    if "D" not in selected:
        selected.append("D")  # Добавляем антидот, если его нет

    # Рассчитываем итоговые очки выживания
    total_points = initial_points + sum(
        next(item["points"] for item in items if item["symbol"] == item_symbol) for item_symbol in selected)

    return selected, total_points


# Вызываем функцию для решения задачи
selected_items, total_points = choose_items(items, backpack_size, initial_points)

# Выводим результат
for row in selected_items:
    print(row)

print(f"Итоговые очки выживания: {total_points}")

print_knapsack_solution(items, designations, values, weights, capacity, K)

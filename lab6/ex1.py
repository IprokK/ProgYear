class Building:
    className = 'Building'

    def __init__(self, area, cost, residents):
        self.area = area
        self.cost = cost
        self.residents = residents

    def total_cost(self):
        return self.area * self.cost

    def ratio(self):
        if self.residents != 0:
            return self.total_cost() / self.residents
        else:
            return 0


class VillageHouse(Building):
    className = 'VillageHouse'

    def __init__(self, area, cost, residents, garden_size):
        super().__init__(area, cost, residents)
        self.garden_size = garden_size

    def garden_ratio(self):
        if self.area != 0:
            return self.garden_size / self.area
        else:
            return 0


class CityApartment(Building):
    className = 'CityApartment'

    def __init__(self, area, cost, residents, num_rooms):
        super().__init__(area, cost, residents)
        self.num_rooms = num_rooms

    def rooms_ratio(self):
        if self.residents != 0:
            return self.num_rooms / self.residents
        else:
            return 0


village_house = VillageHouse(area=100, cost=10000, residents=3, garden_size=500)
print("Общая стоимость: ", village_house.total_cost())
print("Соотношение стоимости к числу проживающих: ", village_house.ratio())
print("Соотношение площади сада к площади дома: ", village_house.garden_ratio())

print('\n')

city_house = CityApartment(area=90, cost=60000, residents=5, num_rooms=3)
print("Общая стоимость: ", city_house.total_cost())
print("Соотношение стоимости к числу проживающих: ", city_house.ratio())
print("Соотношение числа проживающих к количеству комнат: ", city_house.rooms_ratio())

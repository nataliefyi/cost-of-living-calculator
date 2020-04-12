# __author__ = 'Natalie Bright' on (12/3/2019) at (4:17 PM)


class City:

    def display_city_costs(self):
        # print(self.housing)
        # print(self.transportation)
        # print(self.food)
        # print(self.entertainment)
        print(self.cost_of_living)

    def __init__(self,
                 # housing, transportation, food, entertainment,
                 cost_of_living, name):
        # self.housing = housing
        # self.transportation = transportation
        # self.food = food
        # self.entertainment = entertainment
        self.cost_of_living = cost_of_living
        self.name = name

    def get_cost_of_living(self):
        return self.cost_of_living

    def get_name(self):
        return self.name


cities = []

portland = City(1, "Portland")
sanFran = City(1.51, "San Francisco")
seattle = City(1.16, "Seattle")

cities.append(portland)
cities.append(sanFran)
cities.append(seattle)

print(cities[0].name)
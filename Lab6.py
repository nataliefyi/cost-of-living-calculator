# __author__ = 'Natalie Bright' on (11/19/2019) at (7:03 PM)


# This program allows you to compare salaries in cities with different costs of living

# Inputs: current_city.value, current_city.name, offered_city.value, offered_city.name
# Outputs: offered_salary.value, offered_salary.city.name, effective_offer, current_salary.city.name

# Class City
#   Public Function __init__ (self, Integer cost_of_living, String name)
#       Integer self.cost_of_living = Integer cost_of_living
#       String self.name = String name
#   End Module
# End Class


class City:

    def __init__(self, cost_of_living, name):
        self.cost_of_living = cost_of_living
        self.name = name


# Class Salary:
#   Public Function __init__(self, Real value, City city, Real cost_of_living)
#       self.value = value
#       self.city = city
#       self.cost_of_living = cost_of_living

#   @classmethod
#   Public Function get_user_salary(cls, String salary_prompt, String city_prompt)
#       Declare City array cities

#       portland = City(1, "Portland")
#       sanFran = City(1.51, "San Francisco")
#       seattle = City(1.16, "Seattle")

#       cities.append(portland)
#       cities.append(sanFran)
#       cities.append(seattle)
#
#       While True:
#             try:
#                 value = float(input(salary_prompt))
#             except ValueError:
#                 Display ("Salary must be a number greater that 0.")
#                 continue
#             If value <= 0 Then
#                 Display ("Salary must be a number greater that 0.")
#                 continue
#             Else:
#                 break
#             End If
#       End While
#         While True:
#             city_list_array = []
#             for i in range(len(cities)):
#                 city_list_array.append(cities[i].name)
#             city_list = "\n".join(map(str, enumerate(city_list_array)))
#             try:
#                 city_index = int(input(city_prompt + "\n" + str(city_list) + "\n"))
#             except ValueError:
#                 print("Choose a number from the list of cities.")
#                 continue
#             If city_index > (len(city_list_array) - 1) Then
#                 print("Choose a number from the list from the list of cities")
#                 continue
#             Else:
#                 break
#             End If
#       End While
#
#         city = cities[city_index]
#         print(city.name)
#
#         cost_of_living = cities[city_index].cost_of_living
#
#         salary = cls(value, city, cost_of_living)
#         return salary
#   End Function

class Salary:

    def __init__(self, value, city, cost_of_living):
        self.value = value
        self.city = city
        self.cost_of_living = cost_of_living

    @classmethod
    def get_user_salary(cls, salary_prompt, city_prompt):
        cities = []

        portland = City(1, "Portland")
        sanfran = City(1.51, "San Francisco")
        seattle = City(1.16, "Seattle")

        cities.append(portland)
        cities.append(sanfran)
        cities.append(seattle)

        while True:
            try:
                value = float(input(salary_prompt))
            except ValueError:
                print("Salary must be a number greater that 0.")
                continue
            if value <= 0:
                print("Salary must be a number greater that 0.")
                continue
            else:
                break
        while True:
            city_list_array = []
            for i in range(len(cities)):
                city_list_array.append(cities[i].name)
            city_list = "\n".join(map(str, enumerate(city_list_array)))
            try:
                city_index = int(input(city_prompt + "\n" + str(city_list) + "\n"))
            except ValueError:
                print("Choose a number from the list of cities.")
                continue
            if city_index > (len(city_list_array) - 1):
                print("Choose a number from the list from the list of cities")
                continue
            else:
                break

        # noinspection PyUnboundLocalVariable
        city = cities[city_index]
        print(city.name)

        cost_of_living = cities[city_index].cost_of_living

        # noinspection PyUnboundLocalVariable
        salary = cls(value, city, cost_of_living)
        return salary

    # Module get_cost_of_living_ratio(self, City city)
    #   Real col_ratio = Real self.cost_of_living / Real city.cost_of_living
    #   return Integer col_ratio
    # End Module

    def get_cost_of_living_ratio(self, city):
        col_ratio = self.cost_of_living / city.cost_of_living
        return col_ratio

    # Module get_effective_offer(self, Real col_ratio)
    #   Real effective_offer = Real self.value * Real col_ratio
    #   return Real effective_offer
    # End Module
    def get_effective_offer(self, col_ratio):
        effective_offer = self.value * col_ratio
        return effective_offer

    def display_effective_offer(self, effective_offer, current_city_name):
        print("$%.2f" % self.value + " in " + self.city.name + " is equivalent to "
              + "$%.2f" % effective_offer + " in " + current_city_name)


# Function calculator()
#     print("Welcome to the Cost of Living Calculator. This program takes into account cost of living when comparing "
#           "salaries between job offers in Portland, San Francisco and Seattle.")
#     While True:
#         String current_salary_prompt = "What is your current salary?"
#         String current_city_prompt = "Enter a number from the list to select your current city"
#         Salary current_salary = Salary.get_user_salary(current_salary_prompt, current_city_prompt)
#
#         String offered_salary_prompt = "What is the salary you've been offered?"
#         String offered_city_prompt = "Enter a number from the list to select the city your offer is in."
#         Salary offered_salary = Salary.get_user_salary(offered_salary_prompt, offered_city_prompt)
#
#         Real ratio = current_salary.get_cost_of_living_ratio(offered_salary.city)
#
#         Real effective_offer = offered_salary.get_effective_offer(ratio)
#
#         Display("$%.2f" % offered_salary.value + " in " + offered_salary.city.name + " is equivalent to "
#               + "$%.2f" % effective_offer + " in " + current_salary.city.name)
#
#         calc_again = input("Would you like to compare salaries again? Enter Y to start over, or enter any "
#                            "other key to quit: ")
#         If calc_again == "Y" or calc_again == "y" Then
#             continue
#         Else:
#             print("Thank you for using the Cost of Living Calculator")
#             break
#          End If
#       End While
# End Function

def calculator():
    print("Welcome to the Cost of Living Calculator. This program takes into account cost of living when comparing "
          "salaries between job offers in Portland, San Francisco and Seattle.")
    while True:
        current_salary_prompt = "What is your current salary?"
        current_city_prompt = "Enter a number from the list to select your current city"
        current_salary = Salary.get_user_salary(current_salary_prompt, current_city_prompt)

        offered_salary_prompt = "What is the salary you've been offered?"
        offered_city_prompt = "Enter a number from the list to select the city your offer is in."
        offered_salary = Salary.get_user_salary(offered_salary_prompt, offered_city_prompt)

        ratio = current_salary.get_cost_of_living_ratio(offered_salary.city)

        effective_offer = offered_salary.get_effective_offer(ratio)

        offered_salary.display_effective_offer(effective_offer, current_salary.city.name)

        calc_again = input("Would you like to compare salaries again? Enter Y to start over, or enter any "
                           "other key to quit: ")
        if calc_again == "Y" or calc_again == "y":
            continue
        else:
            print("Thank you for using the Cost of Living Calculator")
            break


# Call calculator()
calculator()

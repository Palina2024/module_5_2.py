# Необходимо дополнить класс House следующими специальными методами:
# 1. __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# 2. __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}.'

h1 = House('ЖК Гулливер', 25)
h2 = House('Hytte', 12)


# __str__
print(str(h1))
print(str(h2))

# __len__
print(len(h1))
print(len(h2))
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        print(f"ЖК называется '{self.name}', этажей в доме '{self.number_of_floors}', хочу на '{self.new_floor}' этаж")

    #     if self.number_of_floors < 1 or self.new_floor > self.number_of_floors:
    #         print(f"В ЖК '{self.name}' этажа с номером '{self.new_floor}' не существует")
    #         return
    #     else:
    #         for i in range(1,self.new_floor + 1):
    #             print(i)
    #
    #         print(f"Добро пожаловать на '{self.new_floor}' этаж")
    # def __len__(self):
    #      return self.number_of_floors


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors and self.name == other.name
        return False

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, value + self.number_of_floors)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __str__(self):
        return f"ЖК '{self.name}' количество этажей '{self.number_of_floors}'"



hous = House('Горский', 10)
hous1 = House('Домик в деревне', 20)
hous.go_to(1)
hous1.go_to(1)


print(hous)
print(hous1)
print(hous == hous1)

# print(len(hous)) # __len__
# print(len(hous1)) # __len__
# print(str(hous)) # --str__
# print(str(hous1)) # __str__

  #__eq__


hous = hous + 10  # __add__
print(hous) # __add__


hous.name = 'Домик в деревне'
print(hous == hous1)



hous += 10  # __iadd__
print(hous) # __iadd__
hous1 = 10 + hous1  # __radd_
print(hous1)  # __radd_

print(hous > hous1)  # __gt__
print(hous1 >= hous1) # __ge__
print(hous < hous1)  #__lt__
print(hous1 <= hous1) # __le__
print(hous1 != hous1) # __ne__



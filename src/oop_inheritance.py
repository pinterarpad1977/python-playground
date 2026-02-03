'''
Create two classes:
1. Vehicle
Attributes: brand, year
Method: info() → returns a string

2. Car (inherits from Vehicle)
Extra attribute: doors
Override info() to include number of doors
'''

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} from year {self.year}."
    
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def info(self):
        base = super().info()
        return f"{self.doors} doors {base}"
    

c1 = Car("Toyota", 2020, 4)
print(c1.info())

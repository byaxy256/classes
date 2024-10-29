class vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def method_start(self):
        print(f'{self.brand} started')
class car(vehicle):
    def __init__(self,brand,year,color,number_of_doors):
        super().__init__(brand, year)
        self.color=color
        self.number_of_doors=number_of_doors
    def show_info(self):
        print(f'brand:{self.brand} of year {self.year} with {self.color} and{self.number_of_doors} doors has started.')
class Electriccar(car):
    def __init__(self, brand, year, color, number_of_doors, battery_capacity):
        super().__init__(brand, year, color, number_of_doors)
        self.battery_capacity=battery_capacity
    def show_battery(self):
        print(f'electric_car {self.brand} of year {self.year} with {self.color} color and {self.number_of_doors} doors has started with battery capacity of {self.battery_capacity}%')
my_electric_car=Electriccar('benz',2022,'black',4,87)
my_electric_car.show_battery()
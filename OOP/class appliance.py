class appliance:
    def __init__(self, name, power_consumption,brand):
        self.name=name
        self.power_consumption=power_consumption
        self.brand=brand
class washing_machine(appliance):
    def __init__(self, name, power_consumption, brand, washing_capacity,drum_size):
        super().__init__(name, power_consumption, brand)
        self.washing_capacity=washing_capacity
        self.drum_size=drum_size
    def show_details(self):
        print("Name:", self.name)
        print("Power Consumption:", self.power_consumption, "kW")
        print("Brand:", self.brand)
        print("Washing Capacity:", self.washing_capacity, "kg")
        print("Drum Size:", self.drum_size, "kg")

# Creating objects

washing_machine1 = washing_machine("Samsung Washing Machine", 10, "Samsung", 100, 10)
washing_machine2 = washing_machine("Haier Washing Machine", 8, "Haier", 80, 8)
washing_machine2.show_details()
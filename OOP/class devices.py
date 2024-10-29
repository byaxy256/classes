class device:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}')
class smartphone(device):
    def __init__(self, brand, model, os,storage_capacity, battery_capacity):
        super().__init__(brand, model)
        self.os=os
        self.storage_capacity=storage_capacity
        self.battery_capacity=battery_capacity
    def display_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, OS: {self.os}, Storage Capacity: {self.storage_capacity}, Battery Capacity: {self.battery_capacity}')
my_smartphone=smartphone('Apple','iphone12','ios','128gb','98%')
my_smartphone.display_info()
   
    

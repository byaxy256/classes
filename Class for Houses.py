# Class for Shoes
class Shoe:
    def _init_(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

   
    # Method to get shoe info
    def get_info(self):
        return f"Brand: {self.brand}, Size: {self.size}, Color: {self.color}."

# Usage
shoe = Shoe("Nike", 9, "black")
print(shoe.get_info())  # To get shoe info

# class device:
#     def __init__(self, name, manufacturer, os, screen_size, storage_capacity, processor, camera_specs, battery_capacity, weight):
#         print ("device is operating") 
# class paco:
#     def __init__(device):
#         print('boiling')
        
class shape:
    def __init__(self,type,sides):
        self.type=type
        self.sides=sides
    def area(self):
        print(f"{type}'s Area is:")
class circle:
    def __init__(self, type, radius):
        self.radius=radius
        self.type=type
    def area(self):
        print(f'{self.type}\'s Area is = {self.radius * 2}')
my_circle = circle('circle',12)
my_circle.area()  

# class Square(shape):
#      def area(self, type, sides, length):
#          super().__init__(type, sides)
#          self.length = length

#      def area(self):
#          print(f"{self.type}'s Area is: {self.length * 2}")

# my_square = Square('square', 4, 5)
# my_square.area()

class rectangle(shape):
    def __init__(self, type, sides, length, width):
        super().__init__(type, sides)
        self.length = length
        self.width = width
    def area(self):
        print(f"{self.type}'s Area is: {self.length * self.width}")

my_rectangle = rectangle('rectangle', 4, 5, 6)
my_rectangle.area()

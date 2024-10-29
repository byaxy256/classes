class animal:
    def sound (self):
        print('some generic animal sound...')

class Dog(animal):
    def sound (self):
        print('Bark!.....')
class Cat(animal):
    def sound(self):
        print('Meow!......')
        
def make_animal_sound(animal):
    animal.sound()

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Passing instances to make_animal_sound function
make_animal_sound(dog)  
make_animal_sound(cat) 
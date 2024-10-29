#class for dogs
class Dog:
    def __init__ (self,breed,sex,color):
        self.breed = breed
        self.sex = sex
        self.color = color

    #method to get dog info
    def get_info(self):    
        return f"Dog's breed: {self.breed}, sex: {self.sex} and color: {self.color}."

#usage
dog = Dog("boerbell","male","brown" )
print(dog.get_info())

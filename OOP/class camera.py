class Camera:
    def take_photo(self):
        print("Taking a photo...")

class Phone:
    def make_call(self):
        print("Making a phone call...")

# Child class Smartphone inherits from both Camera and Phone
class Smartphone(Camera, Phone):
    pass

# Create an object of the Smartphone class
smartphone = Smartphone()

# Call both methods
smartphone.take_photo()  # Accessing method from Camera
smartphone.make_call()    # Accessing method from Phone

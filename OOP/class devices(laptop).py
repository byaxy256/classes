# class device:
#     def info(self):
#         print('device information')
# class computer:
#     def info (self):
#         device.info()
#         print('computer information')
# class Laptop(computer):
#     def info (self):
#         super(). info()
#         super(device,self).info()
#         print('laptop information')
# pc = Laptop()
# pc.info()
        
# Base class
class Device:
    def info(self):
        print("Device information")

# Child class Computer that inherits from Device
class Computer(Device):
    def info(self):
        print("Computer information")

# Child class Laptop that inherits from Computer
class Laptop(Computer):
    def info(self):
        # Call the info() method of Computer
        super().info()
        # Call the info() method of Device
        Device.info(self)
        # Laptop's own info message
        print("Laptop information")

# Create an instance of Laptop and call the info method
laptop = Laptop()
laptop.info()

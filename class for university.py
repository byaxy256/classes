#class for university
class University:
    def __init__(self,name,moto,location,branches =1):
        self.name =name
        self.moto =moto
        self.location =location
        self.branches =branches
#method to to get university
    def __str__(self):
        return (f" Name: {self.name}, Moto:{self.moto}, Location:{self.location}, Branches:{self.branches}")

ucu=University('UCU','center of excellence in the heart of africa','mukono')
print(ucu)
muk=University('muk','people power','makerere',4)
print(muk)
kiu=University('kiu','in UCU we trust','sudan',2)
print(kiu)
    
class person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
        
class student(person):
    def __init__(self,name,age,access_no,grade):
        super().__init__(name, age)
        self.access_no = access_no
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f'access_no={self.access_no} Grade={self.grade}')
        
class staff(person):
    def __init__(self, name, age,staffID):
        super().__init__(name, age)
        self.staffID=staffID
        
    def display_info(self):
        super().display_info()
        print(f'staffID={self.staffID}')
        
student = student (name='moze',age='30',access_no='b23727',grade='4.5')
student.display_info()
staff = staff (name='james', age='45',staffID='295474')
staff.display_info()
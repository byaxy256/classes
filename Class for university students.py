class Student:
    def __init__(self, name, reg_no, access_no):
        # Initialize the attributes
        self.name = name
        self.reg_no = reg_no
        self.access_no = access_no

    # Method to display the student's information when printing the object
    def __str__(self):
        return (f"Name: {self.name}, Reg No: {self.reg_no}, Access No: {self.access_no} - fully registered.")

# Creating instances of the Student class
jane_smith = Student('Jane Smith', 'S23B12/001', 'A27364')
mark_peter = Student('Mark Peter', 'S23B13/002', 'B47278')

# Displaying the student information
print(jane_smith)
print(mark_peter)

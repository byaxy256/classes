class employee:
    def employee_status(self):
        print('employee is working.....')
class Manager(employee):
    def work(self):
        print('manager is managing the team.....')
class Developer(employee):
    def work (self):
        print('developer is writing code......')
# Creating objects for both Manager and Developer
manager = Manager()
developer = Developer()

# Calling the work() method for each to demonstrate method overriding
manager.work()     
developer.work()  
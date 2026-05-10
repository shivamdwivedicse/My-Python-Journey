class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

    def ShowDetails(self):
        print(f'The name of Employee: is:{self.name} and id is {self.id}')

class Programmer(Employee):
    def ShowLanguage(self):
        print("My name is shivam dwivedi.")

e1 = Employee("ROHAN" , 420)
e1.ShowDetails()

e2 = Employee("Ram" , 421)
e2.ShowDetails()

e3 = Programmer("Shivam" , 329)
e3.ShowDetails()
e3.ShowLanguage()
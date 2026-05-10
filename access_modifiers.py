# PUBLIC ACCESS MODIFIRE
class Student:
    def __init__(self , name , age):
        self.age = age #public variable
        self.name = name ##public variable

obj = Student("Shivam" , 19)
print(obj.age)
print(obj.name)

# PRIVATE ACCESS MODIFIRE 
class Employee:
    def __init__(self):
        self.__name = "Harry"
a = Employee()
# print(a.__name)
#not able to access but can be accessed indirectly
print(a._Employee__name)

# PROTECTED ACCESS MODIFIRE
class Student:
    def __init__(self):
        self._name = "Shivam"

    def _funcName(self):
        return "CdeWithShivam"
    
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._funcName())

print(obj1._name)
print(obj1._funcName())
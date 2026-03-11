class person:
    name = "Harry"
    occupation = "Software Devloper"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}.")
a = person()
b = person()
a.name="Shivam"
a.occupation = "Accountant"

b.name= "rajesh"
b.occupation = "Teacher"

# print(a.name)
a.info()
b.info()

class student:
    Name = "Shivam"
    Age = 19
    Branch = "B.Tech"

    def info(self):
        print(f"Name :{self.Name} , Age :{self.Age} , Branch :{self.Branch}.")
a = student()
b = student()
c = student()
d = student()
e = student()
f = student()


b.Name ="Aman"
b.Age= 19
b.Branch = "B.Tech"   

c.Name ="Saurabh"
c.Age= 19
c.Branch = "B.Tech"  

d.Name ="Harshit"
d.Age= 19
d.Branch = "B.Tech" 

e.Name ="Mantra"
e.Age= 19
e.Branch = "B.Tech"    

f.Name ="Aman Jyot"
f.Age= 19
f.Branch = "B.Tech"        


a.info()
b.info()
c.info()
d.info()
e.info()
f.info()

class car:
    Name = "BMW"
    Model = 1
    Sale = 22
    Maximum = "1.2CR"

    def info(self):
        print(f"Name :{self.Name} , Model :{self.Model}  ,Sale :{self.Sale} , Maximum :{self.Maximum}.")

c1= car()
c2= car()
c3= car()
c4= car()
c5= car()
c6= car()
c7= car()
c8= car()
c9= car()
c10= car()
c11=car()  
# c1.info()

c2.Name = "Toyota"
c2.Model = 2
c2.Sale = 35
c2.Maximum = "80L"

c3.Name = "Mercedes-Benz"
c3.Model = 3
c3.Sale = 18
c3.Maximum = "2CR"

c4.Name = "Audi"
c4.Model = 4
c4.Sale = 20
c4.Maximum = "90L"

c5.Name = "Tesla"
c5.Model = 5
c5.Sale = 15
c5.Maximum = "1.5CR"

c6.Name = "Honda"
c6.Model = 6
c6.Sale = 40
c6.Maximum = "50L"

c7.Name = "Ford"
c7.Model = 7
c7.Sale = 30
c7.Maximum = "70L"

c8.Name = "Porsche"
c8.Model = 8
c8.Sale = 10
c8.Maximum = "3CR"

c9.Name = "Lamborghini"
c9.Model = 9
c9.Sale = 5
c9.Maximum = "5CR"

c10.Name = "Jaguar"
c10.Model = 10
c10.Sale = 12
c10.Maximum = "2CR"

c11.Name = "Ferrari"
c11.Model = 11
c11.Sale = 6
c11.Maximum = "4CR"


c1.info()
c2.info()
c3.info()
c4.info()
c5.info()
c6.info()
c7.info()
c8.info()
c9.info()
c10.info()
# c11.info()


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def avg(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f'Student: {self.name}')
        print(f'Marks: {self.marks}')
        print(f'Average: {self.avg():.2f}')
        print('------------------------')


# Creating objects
s1 = Student("Shivam")
s2 = Student("Aman")
s3 = Student("Saurabh")

# Adding marks
s1.add_mark(80)
s1.add_mark(75)
s1.add_mark(90)

s2.add_mark(85)
s2.add_mark(70)
s2.add_mark(95)

s3.add_mark(60)
s3.add_mark(78)
s3.add_mark(88)

# Display info
s1.display()
s2.display()
s3.display()


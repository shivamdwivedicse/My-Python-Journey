def area(r):
    pi = 3.14156
    area = pi * r * r
    return area
radius = int(input("Enter the radius :"))
print("The radius is :" , area(radius))

def factorial(num):
    fact = 1
    for i in range (1,num+1):
        fact = fact * i
    return fact
num = int(input("Enter the number :"))
print("The factorial of number",num,"is :" , factorial(num))

def largest():
    a = int(input("Enter 1st number :"))
    b = int(input("Enter 2nd number :"))
    c = int(input("Enter 3rd number :"))

    if a>=b and a>=c:
        print("largest number is a  :", a)
    elif b>=a and b>=c:
        print("Largest number is b :", b)
    else:
        print("The largest number is c  ", c)

largest()
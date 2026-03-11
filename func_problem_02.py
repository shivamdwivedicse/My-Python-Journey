# Calculate area of Rectangle :-
def area_rectangle(length , width):
    return length * width
print("Area of rectangle is :- Length * width")
len = float(input("Enter the length :"))
wid = float(input("Enter the width :"))
print("The area of rectangle is :" , area_rectangle(len , wid))

#perimeter:-

def perimeter_rectangle(length , width):
    return 2 * (length + width) 
print("Perimeter of rectangle is : 2(Length + width)")
len = float(input("Enter the length :-"))
wid = float(input("Enter the width :"))
print("The area of rectangle is :" , perimeter_rectangle(len , wid))
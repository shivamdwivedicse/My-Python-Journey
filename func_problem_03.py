# check the number is even or odd:-
#code:-

def even_odd(num):
    if num % 2 == 0:
        print(f"The {num} is an even number")
    else:
        print(f"The {num} is an odd number ")   
number = int(input("Enter the number :-"))
even_odd(number)
         
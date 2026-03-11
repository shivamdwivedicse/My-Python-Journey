#celcius to farenhite
#code:-
def celcius_to_farenhite(c):
    f = (c*9/5) +32
    return f
temp_c = float(input("Enter the temprature in celcius :"))
print("The temprature in farenhite is :", celcius_to_farenhite(temp_c))
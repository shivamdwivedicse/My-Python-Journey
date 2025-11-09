# 🧩 Problem: Simple Electricity Bill Calculator

# Scenario:
# An electricity company charges different rates based on how much electricity (in units) a household uses in a month.
# You need to calculate the total bill amount for a customer based on their units consumed.

# Rate chart:

# For first 100 units → ₹5 per unit

# For next 100 units (101–200) → ₹7 per unit

# Above 200 units → ₹10 per unit

# Add ₹50 as a fixed meter charge to every bill

#code:-

print("Welcome to the Electricity Charge Calculator based on give information:-")
print("start")
units= int(input("Enter how many units consumed showing on your meter board :-"))
print("Electricity consumed by you in units is :-",units)

bill=0
if units <= 100:
    bill=units*5
elif units<=200:
    bill = (100*5) + (units -100)*7
else:
    bill = (100*5) + (100*7) + (units-200)*10

bill=bill+50
print("Your total bill based on your consumption in units is of Rs:-", bill)
print("Thankyou!")

# Calculate total bill with tax and discount :-
#code:-

def calculate_bill(amount, tax_rate = 0.18 , discount=0.10):
    tax= amount * tax_rate
    discount_amt = amount * discount
    total = amount + tax - discount_amt
    return total
bill = float(input("Enter your purchase amount :"))
final_amount = calculate_bill(bill)   
print(f" Final bill amount with (tax and discount) is : {final_amount}")
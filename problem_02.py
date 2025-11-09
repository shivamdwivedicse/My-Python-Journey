print("Welcome to the discount calculator:-")
purchase = int(input("Enter the amount of total purchase you have done:-"))
print("You purchased items of worth Rs:-", purchase)
discount=0
if purchase <= 500:
    print("Soory! No Discount")
    print("You have to pay Rs :-", purchase)

elif 501<purchase<=1000:
    discount =  (10 * purchase)/100
    final_amount = purchase - discount
    print("Total amount you has to pay is",final_amount )   

else:
    discount =  (20 * purchase)/100
    final_amount = purchase - discount
    print("Total amount you has to pay is",final_amount)

print("Thankyou!")    
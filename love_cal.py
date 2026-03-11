print("Welcome to the LOVE CALCULATOR😉😁💕")
num1=input("ENTER YOUR NAME :-")
num2=input("ENTER YOUR PATNER'S NAME :-")

love_result = len(num1+num2) *5 %100
print(f"😍Your Love result is {love_result}%❤️😉")

if love_result>= 80:
    print("YOU BOTH ARE MADE FOR EACH OTHER 😁💕")
elif love_result >=75:
    print("YOU LOVE EACH OTHER SO MUCH! TAKE TIME AND KNOW WELL TO EACH OTHER 😁💕")  
elif love_result >=50:
    print("Huhhhhh!!! SIRF HAWAS BATAO DONO ME Huhhhhh.")  
else:
    print("Friend Zone Activated😉😁 ")

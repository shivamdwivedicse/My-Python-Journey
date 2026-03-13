# Print numbers from 1 to 20 with rules:

# If number divisible by 3 → print "Fizz"

# If number divisible by 5 → print "Buzz"

# If divisible by both → print "FizzBuzz"

# Otherwise print the number
for i in range(1,21):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

# Check whether a number is prime or not.

num = int(input("Enter the number :"))
if num<=1:
    print("Not Prime.")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not Prime")
            break
    else:
            print("Prime")


# Remove Duplicates from List

lst = [1,2,2,3,3,4,5,5,6,6,7,7]
lst1=[]
for list in lst:
    if list not in lst1:
        lst1.append(list)

print("List after removing duplicates" , lst1) 

# Anagram
word1 = input("Enter First word :")
word2 = input("Enter Seconed word :")

if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not Anagram")


# Program to Print First 10 Fibonacci Numbers

n = 10

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
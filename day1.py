# Write a Python program to calculate the sum of all numbers in a list
lst = [1,2,3,4,5]
Total = sum(lst)
print(Total) 

# Find the largest number in a list without using max().

numbers = [10,40,50,20,60]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num 
print("Maximum number:", maximum)  

# Count how many even and odd numbers are present in a list.

numbers = list(map(int,input("Enter numbers:").split()))
even = 0
odd  = 0

for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1

print("Total even numbers:" , even)
print("Total odd numbers:",odd)            


# Reverse a list without using reverse() or slicing [::-1].

numbers = [10,40,50,20,60]
start = 0
end = len(numbers)-1
while start<end:
    numbers[start] , numbers[end] = numbers[end] , numbers[start]
    start+=1
    end-=1
print("Reversed List:" , numbers)    

# Remove duplicate elements from a list.

numbers = [1,1,2,3,2,4,5,5,5,5,6,6,7,7,7,]
unique =[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List after removing duplicates" , unique) 
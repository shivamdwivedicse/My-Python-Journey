# Reverse a List (Without reverse())
numbers = [1,2,3,4,5]
start = 0
end = len(numbers)-1
while start<end:
    numbers[start] , numbers[end] = numbers[end] , numbers[start]
    start = start +1
    end = end-1
print(numbers)

# Find Missing Number in a List
excepted_list = [1,2,3,4,5,6]
list = [1,2,3,5,6]
for num in excepted_list:
    if num not in list:
        print(num)

# Remove Duplicates From List
numbers = [1,1,2,3,2,4,5,5,5,5,6,6,7,7,7,]
unique =[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List after removing duplicates" , unique) 

# Check if Two Lists Are Equal (Ignoring Order)
list1 = [1,2,3]
list2 = [3,1,2]
list1.sort()
list2.sort()

if list1 == list2:
    print("List are equal.")
else:
    print("Lists are not equal.")

# Create a 3×3 matrix of random numbers and print:
# matrix
# sum of all elements
# mean
# max value
import numpy as np

matrix = np.random.randint(1,10,(3,3))

print(matrix)

print("Sum:", matrix.sum())
print("Mean:", matrix.mean())
print("Max:", matrix.max())
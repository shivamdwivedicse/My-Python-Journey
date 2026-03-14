# Count how many times each word appears in a sentence.

text = "python is great and python is easy"
texts = text.split()

count = {}
for char in texts:
    if char in count:
        count[char] +=1
    else:
        count[char] = 1
print(count)

# Find Most Frequent Element in a List
numbers = [1,2,3,2,4,2,5,3]
count = {}

for num in numbers:
    if num in count:
        count[num]+=1
    else:
        count[num] = 1

max_count = 0
most_frequent = None
for key in count:
    if count[key]>max_count:
        max_count = count[key]
        most_frequent = key
print("Most Frequent element :" , most_frequent)

# Flatten a Nested List
nested_list = [[1,2],[3,4],[5,6]]

flat_list =[]
for sublist in nested_list:
    for num in sublist:
        flat_list.append(num)
print(flat_list)

# Find Second Largest Number

numbers = [10,45,23,67,12]
largest = numbers[0]
seconed_largest = numbers[0]
for num in numbers:
    if num>largest:
        seconed_largest = largest
        largest = num 
    elif num>seconed_largest and num!=largest:
        seconed_largest = num 
print("Seconed Largest :" , seconed_largest)

# Matrix Transpose

matrix = [[1,2,3],[4,5,6]]
rows = len(matrix)
cols = len(matrix[0])

transpose = []

for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)
print(transpose)
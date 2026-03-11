# lst = [1,2,3,4,5]
# Total = sum(lst)
# print(Total) 

# numbers = [10,40,50,20,60]
# maximum = numbers[0]
# for num in numbers:
#     if num > maximum:
#         maximum = num 
# print("Maximum number:", maximum)    

# numbers = list(map(int,input("Enter numbers:").split()))
# even = 0
# odd  = 0

# for num in numbers:
#     if num%2==0:
#         even+=1
#     else:
#         odd+=1

# print("Total even numbers:" , even)
# print("Total odd numbers:",odd)            



# numbers = [10,40,50,20,60]
# start = 0
# end = len(numbers)-1
# while start<end:
#     numbers[start] , numbers[end] = numbers[end] , numbers[start]

#     start+=1
#     end-=1
# print("Reversed List:" , numbers)    



numbers = [1,1,2,3,2,4,5,5,5,5,6,6,7,7,7,]

unique =[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List after removing duplicates" , unique) 
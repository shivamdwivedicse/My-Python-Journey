lst = [0,1,0,3,12]

result = []
#add non zero values first :-
for num in lst:
    if num!=0:
        result.append(num)

#now add zeros at last 
zeros = lst.count(0)
result.extend([0]*zeros)
print(result)



#pair sum 
lst = [2,4,3,5,7]
target = 9
seen = set()
for num in lst:
    diff = target - num
    if diff in seen:
        print(num,diff)
        break
    seen.add(num)

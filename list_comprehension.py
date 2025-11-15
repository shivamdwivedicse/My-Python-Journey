l1=[2,4,6,8,13,14,25,23,35,33]
even= [x for x in l1  if x%2==0]
print(even)

lst = [x for x in range(5)]
print(lst)


squares = [x*x for x in range(1, 6)]
print(squares)

result = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 11)]
print(result)  

pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)

names = ["Shivam", "Amit", "Saurabh"]
first_letters = [name[0] for name in names]
print(first_letters)

fruits = ["apple", "banana", "mango"]
upper = [f.upper() for f in fruits]
print(upper)

vowels = [c for c in "python programming" if c in "aeiou"]
print(vowels)



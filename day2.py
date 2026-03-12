# Reverse a String (without slicing)
text = "Shivam"
rev = ""
for char in text:
    rev = char+rev

print(rev)

# Count Vowels in a String
text = "Programming"
vowels ="aeiou"
count = 0

for char in text:
    if char in vowels:
        count +=1
print("Vowels",count)

# Check Palindrome
text ="madam"
rev =""

for char in text:
    rev = char+rev
if text ==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Count Characters in String
text ="Hello"
char_count={}

for char in text:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] =1

print(char_count)

# Find Longest Word in Sentence
sentence = "I love learning python programming"

words = sentence.split()
longest =""

for word in words:
    if len(word)>len(longest):
        longest = word

print("Longest word:", longest)
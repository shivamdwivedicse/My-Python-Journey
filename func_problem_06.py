# counting vowels in a string 
#code:-

def count_vowels(text):
    vowels ="aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count+=1
    return count
sentence = input("Enter a sentence :")
print("Total vowels :" , count_vowels(sentence))        
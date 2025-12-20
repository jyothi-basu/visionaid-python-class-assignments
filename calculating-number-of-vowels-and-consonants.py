# Calculating number of vowels and consonants.

user= input("Please enter some text: ")
vowels= "aeiou"
vowels_count= 0
consonants_count= 0
for char in user:
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        consonants_count += 1

print("number of vowels:", vowels_count)
print("Number of consonants:", consonants_count)
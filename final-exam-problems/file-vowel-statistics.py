# Printing number of vowels in file and printing number of unique vowels and top 3 unique vowels.

fh= open("q42_sample.txt", "r")
file_content= fh.read()
fh.close()

vowels= "aeiou"
vowel_count= 0
unique_vowels= {}

for char in file_content:
    char= char.lower()
    if char in vowels:
        vowel_count += 1
        if char in unique_vowels:
            unique_vowels[char] += 1
        else:
            unique_vowels[char] = 1

top_unique_vowels = sorted(
    unique_vowels.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Number of vowels are: ", vowel_count)
print("Number of unique vowles are:", len(unique_vowels))
print("Top 3 unique vowels are:")
print(top_unique_vowels[0])
print(top_unique_vowels[1])
print(top_unique_vowels[2])
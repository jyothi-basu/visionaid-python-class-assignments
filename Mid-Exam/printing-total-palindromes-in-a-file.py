# Printing total palindromes in a file.

file1= open("anna_the_palindrome_girl.txt", "r")
file_contents= file1.read()
file1.close()

palindromes_count= 0
words= file_contents.split()

file2= open("Jyothibasu_palindromes.txt", "w")
for word in words:
    if word == word[::-1] and len(word) > 1:
        file2.write(word + "\n")
        palindromes_count += 1
file2.close()
print("Total palindromes in story: ", palindromes_count)
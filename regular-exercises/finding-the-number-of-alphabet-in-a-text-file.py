# Finding the number of alphabet in a text file.

file= open("mbox-short.txt", "r")
alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
file_contents= file.read()
file.close()
alphabet_count= 0
for char in file_contents:
    if char in alphabet:
        alphabet_count += 1
print("Number of alphabet in this file are: ", alphabet_count)
# Calculating number of lines, words and characters in a file.

line_count= 0
word_count= 0
file= open("Data.txt", "r")
for line in file:
    line_count += 1
print("Number of lines: ", line_count)
file.close()

file= open("Data.txt", "r")
for line in file:
    words= line.split()
    word_count += len(words)
print("Number of words: ", word_count)
file.close()

file= open("Data.txt", "r")
char= file.read()
print("Number of characters: ", len(char))
file.close()
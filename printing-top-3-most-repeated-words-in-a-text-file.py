# Printing top 3 most repeated words in a file.

fh= open("twinkle.txt", "r")
file_contents= fh.read()
fh.close()
file_contents= file_contents.strip()
file_contents= file_contents.lower()
words= file_contents.split()
words_list= {}
for word in words:
    words_list[word]= words.count(word)

words_tuple= []
for key in words_list:
    words_tuple.append((words_list[key], key))

words_tuple.sort(reverse= True)
print("Top 3 repeated words in this file are: ")
for t in words_tuple[:3]:
    print(t[1], ":", t[0])
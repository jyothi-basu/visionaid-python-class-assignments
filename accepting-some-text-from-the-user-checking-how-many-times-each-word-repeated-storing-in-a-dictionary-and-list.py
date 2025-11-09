# Accepting some text from the user, checking how many times each word repeated and storing in a dictionary.

text= input("Please enter your text: ")
text.strip()
words= text.split()
words_list= {}

for word in words:
    if word == word:
        count= words.count(word)
        words_list[word]= count
print(words_list)

# Accepting some text from the user, checking how many times each word repeated and storing in a list.

text= input("Please enter your text: ")
text.strip()
words= text.split()
words_list= []
for word in words:
    if word in words_list:
        continue
    else:
        words_list.append(word)
        words_list.append(words.count(word))
print(words_list)
# Developing Program to read input from a file, identify and correct spelling mistakes
# using a dictionary, and write the corrected text to an output file.

fh= open("q46_mistakes.txt", "r")
file_content= fh.read()
fh.close()

file_content= file_content.lower()
file_content= file_content.strip()
text_list= file_content.split()

corrections = { 
    "implimentation": "implementation",
    "beter": "better",
    "obvius": "obvious",
    "ambiguty": "ambiguity",
    "practicalty": "practicality",
    "readabilty": "readability"
}

for i in range(len(text_list)):
    if text_list[i] in corrections:
        text_list[i] = corrections[text_list[i]]
    else:
        continue

text= " ".join(text_list)

fh= open("correction.txt", "w")
fh.write(text)
fh.close()
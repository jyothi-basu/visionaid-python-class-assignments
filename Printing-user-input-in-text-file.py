user= input("Please enter some text: ")

file= open("Notes.txt", "a")
file.write(user)
file.close()
print(“Your text has been saved successfully.”)
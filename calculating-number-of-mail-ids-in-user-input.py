# Calculating number of mail IDs in user input.

gmail= "@gmail.com"
outlook= "@outlook.com"
number_gmail= 0
number_outlook= 0
while True:
    user= input("Please enter the email id: ")
    if gmail in user:
        number_gmail += 1
    elif outlook in user:
        number_outlook += 1
    elif user == "done":
        break

print("Number of gmail IDs:", number_gmail)
print("Number of outlook mail IDs:", number_outlook)
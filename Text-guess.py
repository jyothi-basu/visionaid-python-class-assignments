while True:
    user= input("Please enter some text: ")
    if user== "":
        continue
    elif user== "done":
        print("Correct!")
        break
    else:
        print(user)
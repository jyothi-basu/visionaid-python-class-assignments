total= 0
user= input("Please enter the city you want to visit: ")
for city in user:
    if city == " ":
        continue
    else:
        print(city)
        total += 1

print("Total characters in your city are: ", total)
password = input("Please enter your password to check its strength: ")

length = 0
upper_case = 0
lower_case = 0
even_number = 0
odd_number = 0
special_symbol = 0

if len(password) >= 5:
    length += 1

for char in password:
    if char >= "A" and char <= "Z":
        upper_case += 1
    if char >= "a" and char <= "z":
        lower_case += 1
    if char >= "0" and char <= "9":
        number = int(char)
        if number % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    if char in "$_@":
        special_symbol += 1

if length > 0 and upper_case > 0 and lower_case > 0 and even_number > 0 and odd_number > 0 and special_symbol > 0:
    print("Good Password!")
else:
    print("Not Good password!")
#   This program generates 7 random integers within a user-specified range. 
#   Each number is checked to determine whether it is even or odd.
#   Even numbers are stored in 'Jyothibasu_Evens.txt' and odd numbers in 'Jyothibasu_Odds.txt'.
#   At the end, the program displays how many even and odd numbers were generated.

import random

even_numbers= 0
odd_numbers= 0
low_value= int(input("Please Enter 1st value: "))
high_value= int(input("Please enter 2nd value: "))

r1= random.randint(low_value,high_value)
r2= random.randint(low_value,high_value)
r3= random.randint(low_value,high_value)
r4= random.randint(low_value,high_value)
r5= random.randint(low_value,high_value)
r6= random.randint(low_value,high_value)
r7= random.randint(low_value,high_value)

if r1%2 ==0:
    file= open("Evens.txt", "a")
    file.write(str(r1) + "\n")
    even_numbers += 1
    file.close()
elif r1%2 != 0:
    file= open("Odds.txt", "a")
    file.write(str(r1) + "\n")
    odd_numbers += 1
    file.close()

if r2%2 ==0:
    file= open("Evens.txt", "a")
    file.write(str(r2) + "\n")
    even_numbers += 1
    file.close()
elif r2%2 != 0:
    file= open("Odds.txt", "a")
    file.write(str(r2) + "\n")
    odd_numbers += 1
    file.close()

if r3%2 ==0:
    file= open("Evens.txt", "a")
    file.write(str(r3) + "\n")
    even_numbers += 1
    file.close()
elif r3%2 != 0:
    file= open("Odds.txt", "a")
    file.write(str(r3) + "\n")
    odd_numbers += 1
    file.close()

if r4%2 ==0:
    file= open("Evens.txt", "a")
    file.write(str(r4) + "\n")
    even_numbers += 1
    file.close()
elif r4%2 != 0:
    file= open("Odds.txt", "a")
    file.write(str(r4) + "\n")
    odd_numbers += 1
    file.close()

if r5%2 ==0:
    file= open("Evens.txt", "a")
    file.write(str(r5) + "\n")
    even_numbers += 1
    file.close()
elif r5%2 != 0:
    file= open("Odds.txt", "a")
    file.write(str(r5) + "\n")
    odd_numbers += 1
    file.close()

if r6 %2 ==0:
    file= open("Evens.txt", "a")
    file.write(str(r6)+ "\n")
    even_numbers += 1
    file.close()
elif r6%2 != 0:
    file= open("Odds.txt", "a")
    file.write(str(r6) + "\n")
    odd_numbers += 1
    file.close()

if r7 %2 ==0:
    file= open("Evens.txt", "a")
    file.write(str(r7))
    even_numbers += 1
    file.close()
elif r7%2 != 0:
    file= open("Odds.txt", "a")
    file.write(str(r7))
    odd_numbers += 1
    file.close()

print("Total Even numbers generated: ", even_numbers)
print("Total Odd numbers generated: ", odd_numbers)
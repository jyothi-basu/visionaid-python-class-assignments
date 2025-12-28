# Developing a program to create a list of fifteen randomly generated integers and output the following:
#All ODD numbers greater than the average of the EVEN numbers in the list created.
#All EVEN numbers greater than the average of the ODD numbers in the list created.

## Defining required functions.
## Defining average.
def average(x):
    if len(x) == 0:
        return 0
    return sum(x) / len(x)

## Main program.
import random
rand_nums= []

for n in range(15):
    rand_nums.append(random.randint(1, 100))

rand_even_nums= []
rand_odd_nums= []

for n in rand_nums:
    if n%2==0:
        rand_even_nums.append(n)
    else:
        rand_odd_nums.append(n)

even_nums_average= average(rand_even_nums)
odd_nums_average= average(rand_odd_nums)

print("even numbers > odd numbers' average: ")
for n in rand_even_nums:
    if n > odd_nums_average:
        print(n)
    else:
        continue

print("Odd numbers > even numbers' average: ")
for n in rand_odd_nums:
    if n > even_nums_average:
        print(n)
    else:
        continue
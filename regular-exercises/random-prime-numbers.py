# Creating 10 random numbers and printing prime numbers in it.

nums_list= []
import random
for r in range(10):
    nums_list.append(random.randint(2,100))
nums_tuple= tuple(nums_list)
print("All numbers: ", nums_tuple)
print("Prime numbers: ")
for n in nums_tuple:
    for i in range(2, n):
        if n%i == 0:
            break
    else:
        print(n)
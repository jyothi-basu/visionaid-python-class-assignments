# Creating 2 tuples:
# 1) contains numbers entered by the user
# 2) contains numbers with even numbers removed

nums_list1= []
nums_list2= []
while True:
    nums= input("Please enter your number or 'done' to finish: ")
    if nums.lower()== "done":
        break
    else:
        nums= int(nums)
        nums_list1.append(nums)

nums_tuple1= tuple(nums_list1)

for n in nums_tuple1:
    if n%2 != 0:
        nums_list2.append(n)

nums_tuple2= tuple(nums_list2)
print("Original tuple: ", nums_tuple1)
print("Tuple without even numbers: ", nums_tuple2)
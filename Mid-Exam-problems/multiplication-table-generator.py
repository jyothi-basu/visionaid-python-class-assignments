# Writing a table builder.

number= int(input("Please enter your number: "))
limit= int(input("Please enter your limit for multiplecation: "))
count= 1
while count <= limit:
    print(count * number)
    count += 1
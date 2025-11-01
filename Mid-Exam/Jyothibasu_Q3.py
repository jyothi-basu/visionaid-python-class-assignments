
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Division:", x/y)

except ValueError:
    print("Invalid input please try again!")
except ZeroDivisionError:
    print("Error! divisible by 0 is not possible. please try again.")
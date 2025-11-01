try:
    #nested if
    num1=int(input("Please enter the 1st number: "))
    num2=int(input("Please enter the 2nd number: "))
    if num1>num2:
        print("the 1st number is greater than the 2nd number!")
    else:
        if num1==num2:
            print("Both numbers are equal!")
        else:
            print("the 1st number is lesser than the 2nd number!")

except ValueError:
    print("Please enter a valid number! do not use desimals.")
#a simple calculator
#functions
def sum(num1, num2):
    print("Answer is: ", num1 + num2)

def sub(num1, num2):
    print("Answer is: ", num1 - num2)

def mul(num1, num2):
    print("Answer is: ", num1 * num2)

def div(num1, num2):
    print("Answer is: ", num1 / num2)

#main program
method= input("Please select the method of calculation (+, -, *, /)? ")
num1= float(input("Please enter the 1st number: "))
num2= float(input("Please enter the 2nd number: "))
if method=="+":
    sum(num1,num2)
elif method=="-":
    sub(num1,num2)
elif method=="*":
    mul(num1,num2)
else:
    div(num1,num2)
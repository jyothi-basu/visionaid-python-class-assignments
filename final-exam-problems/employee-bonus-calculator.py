# Developing a program that can iterates through the salary and service lists using index values, applies conditional logic to determine bonus eligibility, and prints the salary statement for each employee.

salary  = [30000, 18000, 21500, 11000, 9500, 13000]
service = [14, 7, 10, 3, 4, 5]

print("Employee Salary statements: ")

for i in range(len(salary)):
    print("Employee ", i+1, "salary statement: ")
    print("Present Salary: Rs. ", salary[i])
    print("Service Period: ", service[i], " Years.")
    print("Eligible % of Bonus: ")
    if service[i] > 10:
        print(10, "%")
        bonus_percent = 10
    elif service[i] >= 6 and service[i] <= 10:
        print(6, "%")
        bonus_percent = 6
    elif service[i] >= 4:
        print(4, "%")
        bonus_percent = 4
    else:
        print(0, "%")
        bonus_percent = 0
    print(" Eligible Amount of Bonus: Rs.", bonus_percent/100*salary[i])
    bonus_amount= bonus_percent/100*salary[i]
    print("New Salary: Rs.", salary[i]+ bonus_amount)
    print("% Hike in Salary: ", bonus_amount/salary[i]*100)
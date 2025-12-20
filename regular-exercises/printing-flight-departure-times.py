# Printing flight departure times.

start= int(input("Please enter the start hour: "))
end= int(input("Please enter the end hour: "))
for hour in range(start, end+1):
    if hour % 12 == 0:
        print(hour)
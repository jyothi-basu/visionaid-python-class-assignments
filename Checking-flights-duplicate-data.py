# Checking flights duplicate data.

file = open("Flights.txt")

previous_line = ""

for line in file:
    current_line = line.strip()
    if current_line != previous_line:
        print(current_line)
        previous_line = current_line
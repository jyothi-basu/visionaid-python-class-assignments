file= open("Airlines.txt")
airline1= 0
airline2= 0
airline3= 0
airline4= 0
airline5= 0
airline6= 0
airline7= 0
for line in file:
    if "Emirates" in line:
        airline1 += 1
    elif "Lufthansa" in line:
        airline2 +=1
    elif "Qatar" in line:
        airline3 += 1
    elif "AirIndia" in line:
        airline4 += 1
    elif "Multiple" in line:
        airline5 += 1
    elif "Kuwait" in line:
        airline6 += 1
    elif "Etihad" in line:
        airline7 += 1

high_bookings= airline1
airline_name = "Emirates"
if airline2 > high_bookings:
    high_bookings = airline2
    airline_name= "Lufthansa"
if airline3 > high_bookings:
    high_bookings = airline3
    airline_name = "Qatar"
if airline4 > high_bookings:
    high_bookings = airline4
    airline_name = "AirIndia"
if airline5 > high_bookings:
    high_bookings = airline5
    airline_name = "Multiple"
if airline6 > high_bookings:
    high_bookings = airline6
    airline_name = "Kuwait"
if airline7 > high_bookings:
    high_bookings = airline7
    airline_name = "Etihad"

print("Airline with high bookings: ", airline_name, "with", high_bookings, "bookings")
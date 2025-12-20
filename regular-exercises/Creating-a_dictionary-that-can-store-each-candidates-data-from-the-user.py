#Creating a dictionary that can store each candidate's data from the user.

data= {}
while True:
    name= input("Please enter the candidate's name or done to finish: ")
    if name.lower()== "done":
        break
    candidate_name= "Name: " + name
    candidate_age= int(input("Please enter the candidate's age: "))
    candidate_favourite_subject= input("Please enter candidate's favourite subject: ")
    data[candidate_name]= {"Age": candidate_age, "Favourite subject": candidate_favourite_subject}
print(data)
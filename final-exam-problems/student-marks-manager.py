# storing student marks in different subjects then printing desired student's marks then printing minimum and maximum marks scored by  students.

## Defining required functions.
## Defining user input function.
def user_input(student_data):
    student_name= input("Please enter the student's name: ")
    student_data[student_name] = {}

    while True:
        subject= input("Please enter the subject's name or 'done' to finish: ")
        if subject.lower() == 'done':
            return student_data
        subject_marks= float(input("Please enter the marks for the subject: "))
        student_data[student_name][subject] = subject_marks

## Defining printing desired student's marks.
def get_marks(student_data):
    desired_student= input("Please enter student's name to see the marks: ")
    if desired_student in student_data:
        for subject in student_data[desired_student]:
            print(subject, student_data[desired_student][subject])
    else:
        print("Student not found")
        return

## Printing students names with minimum and maximum marks.
def min_max(student_data):
    if not student_data:
        print("Student information is unavailable! please add first.")
        return
    students_list= []
    for student in student_data:
        total = sum(student_data[student].values())
        students_list.append((student, total))

    min_student = min(students_list, key=lambda x: x[1])
    max_student = max(students_list, key=lambda x: x[1])
    print("Student with minimum marks: ", min_student)
    print("Student with maximum marks: ", max_student)

## Defining the main menu.
def main_menu():
    input("Welcome to Student marks list manager program! press enter to continue")
    student_data= {}

    while True:
        print("press (1) to add student info.")
        print("Press (2) to see the students info.")
        print("Press (3) to know minimum and maximum marks of the students.")
        choice= input("Please choose an option between 1 and 3")
        if choice == "1":
            user_input(student_data)
        elif choice== "2":
            get_marks(student_data)
        elif choice== "3":
            min_max(student_data)
        else:
            print("Please enter a number between 1 and 3")

## Main program.
main_menu()
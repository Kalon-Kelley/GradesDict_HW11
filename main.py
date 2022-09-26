"""*******************************************************
CS 104: Grades Dict
Description: Make a dictionary where peoples grades are stored
Date: 11/20/2019
Author(s): Lucas Kelley
*******************************************************"""

command = ""
gradesDict = {}

while command != 'Q':

    command = input("""What would you like to do
[A] to add student 
[R] to remove student 
[M] to modify grades 
[P] to print all grades
[Q] to quit
""").upper()

    if command == "A":
        name = input("What is the name of the student you wish to add ").lower()
        grade = input("what is the grade you wish to enter ").upper()
        gradesDict[name] = grade

    elif command == "R":
        name = input("What is the name of the student you wish to remove ").lower()
        try:
            gradesDict.pop(name)
        except KeyError:
            print("\033[91mStudent does not exist\033[00m")

    elif command == "M":
        name = input("What is the name of the student which you want to modify ").lower()
        try:
            print("\033[91m[%s]\033[00m is the grade of the specified student" %gradesDict[name])
            nGrade = input("Enter the new grade you wish to enter in place of the old one ").upper()
            gradesDict[name] = nGrade
        except KeyError:
            print("\033[91mStudent does not exist\033[00m")

    elif command == "P":
        print(gradesDict)

    elif command == "Q":
        print("\033[91mYou have quit the program")
        break

    else:
        print("\033[91mSpecified command does not exist\033[00m")
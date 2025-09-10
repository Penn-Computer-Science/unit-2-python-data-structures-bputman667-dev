studentGrade = {
    "jeff": [12.0, 35.0, 62.0],
    "rob": [16.0, 79.0, 92.0],
    "ralph": [20.0, 20.0, 90.0],
}


def viewGrades(student):
    if(student == "all"):
        for i in studentGrade:
            if(studentGrade[i] != []):
                average = sum(studentGrade[i])/len(studentGrade[i])
                print("the grades of " + i + " are " + str(studentGrade[i]))
                print("the average is " + str(average))
                if(average < 60):
                    print("that's an F")
                elif(average < 70):
                    print("that's a D")
                elif(average < 80):
                    print("that's a C")
                elif(average < 90):
                    print("that's a B")
                else:
                    print("that's an A")
            else:
                print("no grades for " + i)
    else:
        if(student in studentGrade):
            if(studentGrade[student] != []):
                average = sum(studentGrade[student])/len(studentGrade[student])
                print("the grades of " + student + " are " +str(studentGrade[student]))
                print("the average is " + str(average))
                if(average < 60):
                    print("that's an F")
                elif(average < 70):
                    print("that's a D")
                elif(average < 80):
                    print("that's a C")
                elif(average < 90):
                    print("that's a B")
                else:
                    print("that's an A")
            else:
                print("there are no grades for that student")
        else:
            print("that student is not in the gradebook")


def averageDict():
    avgDict = {}
    for i in studentGrade:
        if(studentGrade[i] != []):
            avgDict[i] = sum(studentGrade[i])/len(studentGrade[i])
        else:
            a = 1
    return avgDict


def addStudent(student):
    studentGrade[student] = []


def removeStudent(student):
    studentGrade.pop(student)


def addGrade(student, grade):
    studentGrade[student].append(grade)


def removeGrade(student, grade):
    studentGrade[student].remove(grade)


while(True):
    printedDict = averageDict()
    choice = input("what do you want to do. type 1 to view grade, 2 to add students, type 3 to remove student, type 4 to add grade, type 5 to remove grade, type 6 to view grades in order of lowest to highest ")
    if(choice ==  "1"):
        studentViewed = input("who do you want to view the grade of? type all to view all grades: ")
        viewGrades(studentViewed)
    elif(choice == "2"):
        addedStudent = input("what is the name of the student you want to add? ")
        if(addedStudent not in studentGrade):
            addStudent(addedStudent)
        else:
            print("student is already in gradebook")
    elif(choice == "3"):
        removedStudent = input("what student do you want to remove from the gradebook? ")
        if(removedStudent in studentGrade):
            removeStudent(removedStudent)
        else:
            print("that student is not in the gradebook")
    elif(choice == "4"):
        studentAdded = input("what student are you adding this grade to? ")
        if(studentAdded in studentGrade):
            gradeAdded = (input("what is the grade you want to add? "))
            try:
                gradeAdded = float(gradeAdded)
                addGrade(studentAdded, gradeAdded)
            except ValueError:
                print("that's not a number")
        else:
            print("that student is not in the gradebook")
    elif(choice == "5"):
        removedStudent = input("what student are you trying to remove a grade from? ")
        if(removedStudent in studentGrade):
            removedGrade = (input("what grade are you trying to remove? "))
            try:
                removedGrade = float(removedGrade)
                if(removedGrade in studentGrade[removedStudent]):
                    removeGrade(removedStudent, removedGrade)
                else:
                    print("that grade is not in the gradebook")
            except ValueError:
                print("that's not a number")
    elif(choice == "6"):
        sortedDict = dict(sorted(averageDict().items(), key = lambda x:x[1]))
        for i in sortedDict:
            print(i + " has a " + str(sortedDict[i]))
        print(sortedDict[i])
    else:
        print("that's not a choice")
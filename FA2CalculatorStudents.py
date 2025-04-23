import getpass #imports getpass
ticket = True   #Makes the ticket for the original while loop true 
studentInput = True #Makes the studentsInput true for the while loop
con = "n"   #Makes con start off as no so you have to type y to continue
menu = True #Makes sure the menu while loop keeps going
Student = {}    #declares student as a dictionary

def getGrade(avg):      #Creates a function to determine the grade of the student
    if avg >= 90:       #Checks if the average is above or = to 90
        return "A"
    elif avg >= 80:     #Checks if the average is above or = to 80
        return "B"
    elif avg >= 70:     #Checks if the average is above or = to 70
        return "C"
    elif avg >= 60:     #Checks if the average is above or = to 60
        return "D"
    else:
        return "F"      #The remainding grades are F

def calculation(mark1: float, mark2: float, mark3: float):      #gets the input for the calculation average
    avgPercent = ((mark1 + mark2 + mark3)/300)*100              #Uses the inputs to calculate the average
    return avgPercent                                           #returns the average

def printStudent(name, info):                                   #This creates the function and requires the students name and the info for the dictionary
    print(f"Name: {name}")                                      #Prints the name which it would get from the beginning of the function
    print(f"Maths: {info['Maths']}")                            #Prints the info about maths which it gets from the array
    print(f"Science: {info['Science']}")                        #Prints the info about Science which it gets from the array
    print(f"English: {info['English']}")                        #Prints the info about English which it gets from the array
    print(f"Average: {info['Average']:.2f}")                    #Prints the info about Average which it gets from the array
    print(f"Grade: {info['Grade']}\n")                          #Prints the info about Grade which it gets from the array

while ticket:                                                   #Initiates the while loop
    username = input("Enter your username ")                    #Gets a username from the user
    password = getpass.getpass("Enter your password ")          #Gets a password while making it invisible from the user
    if (password == "admin123") & (username == "Admin"):        #Checks if the password and username are the correct ones to proceed with the program
        print("You Have gained access")                         #Prints you have gained access
        ticket = False                                          #Makes the ticket false which ends the while loop
    else: print("password or username incorrect try again")     #If the password or username is incorrect prints inccorrect and to try again



while studentInput:                                             #Initiates the while loop
    name = input("Enter the Students name: ")                   #Gets the name from the user
    maths = float(input("Enter Maths mark: "))                  #Gets the Maths mark from the user
    science = float(input("Enter Science mark: "))              #Gets the Science mark from the user
    english = float(input("Enter English mark: "))              #Gets the English mark from the user
    average = calculation(maths, science,  english )            #Calculates the average using the average function from earlier
    print(average)                                              #Prints the average so that you can keep track of it in your prompt
    grade = getGrade(average)                                   #Makes the grade using the getGrade function discussed earlier
    print(grade)                                                #Prints the grade so that you can keep track of it in your prompt

    Student[name]= {                                            #Declares the Student array and uses name to keep track of it
    "Maths": maths,                                             #Makes math what the users input
    "Science" : science,                                        #Makes Science what the users input
    "English" : english,                                        #Makes English what the users input
    "Average" : average,                                        #Makes average what was determined earlier
    "Grade" : grade,                                            #Makes grade what was determined earlier
    }

    con = input("Do you wish to keep adding students, type y/n: ")      #checks if you would like to continue and if you don't you must press n
    if con.lower() == "n":                                              #checks if you pressed n so that it can stop the loop
        studentInput = False                                            #makes the while loop end


while menu:                                                                                                                                 #Creates the while loop for the menu
    options = int(input("Press 1 to print all students, press 2 to print a specific student. Type 0 to exit the program: "))                #Checks if the user would like to pick on of the options
    if options == 1:                                                                                                                        #If the user picks 1 it will follow this path
         for name, info in Student.items():                                                                                                 #It will create a loop for all the names and info in the array student and its items
            printStudent(name, info)                                                                                                        #Prints the name and students info
    elif options == 2:                                                                                                                      #Checks if option 2 has been selected
         studentSearch = input("Enter the name of specific student: ")                                                                      #Creates a student search variable to get the name the user wants to search
         printStudent(studentSearch, Student[studentSearch])                                                                                #Prints the information about the student that is searched
    elif options == 0:                                                                                                                      #Checks if option 0 has been selected
         menu = False                                                                                                                       #Ends the menu by making it = false
    else:                                                                                                                                   #Final catch for errors
        print("Invalid try again")                                                                                                          #Lets the user know to try again
#Because we are asking for their age to work out their birth year, we will need to import the datetime module
import datetime

#Greeting user, and giving basic instructions
print("\n* Welcome to HAHA, the Huawow Alumni Hacking Algorithm. *\n\n* When you enter nothing in response to the First Name, the program will end. *")

#setting initial variables, and not using a blank value for "First" as that is the required command for stopping the program
First = "Overridden"

#settling up a log for tracking our results
ConcatenatedResultLog = []

#while loop will run until someone enters a blank "First"
while First != "":
    #while adding a new line break for easier reading
    print("")
    #prompting for the first name 
    First = input("First name only: ")
    #if this is left blank, the program ends, so here is that script
    if First == "":
        break
    #removing any accidental extra spaces from the start or end of the input
    FirstName = First.strip()
    #making the first name all lower case as we don't need to ever have it capitalised
    FirstNameLower = FirstName.lower()
    #identifying the initial or the first name
    FirstNameInitial = FirstNameLower[0]
    #prompting for the last name
    Last = input("Last name only: ")
    #removing any accidental extra spaces from the start or end of the input
    LastName = Last.strip()
    #making the last name all lower case for use in the generated password and email
    LastNameLower = LastName.lower()
    #making a version of the last name all upper case in order to create an upper case initial
    LastNameUpper = LastName.upper()
    #identifying the initial or the last name
    LastNameInitial = LastNameUpper[0]
    #setting the date to right now
    Date = datetime.datetime.now()
    #asking for the age
    Age = int(input("Age (whole number): "))
    #calculating the birth year on the assumption they were born Jan 1, and subtracting lucky number 8 from the result
    BirthYear = Date.year - Age -8
    #creating the final email address and password guesses based on the inputted information
    ConcatenatedResult = (FirstNameInitial+LastNameLower+"@Huawow.io|"+FirstNameLower+LastNameInitial+"_"+str(BirthYear))
    #adding the concatenated result to the log 
    ConcatenatedResultLog.append(ConcatenatedResult)
#Once the loop has been broken, the program will jump to this point and it will print the final log list, with some additional new line breaks for easier reading
print("\nThe final log of results is:")
print(ConcatenatedResultLog,"\n")
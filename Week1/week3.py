#if (y==20):
#   x=9

#if (y>100):
#   x=40
#else:
#   x=20

#num1 = int(input("Enter number 1, it can be a result from 0 to 100: "))
#num2 = int(input("Enter number 2, it can be a result from 0 to 100: "))
#num3 = int(input("Enter number 3, it can be a result from 0 to 100: "))
#avg = float((num1+num2+num3)/3)

#print(avg)

#if (avg > 90):
#    print("Congratulations")
#else:
#    print("You have brought shame upon your family")

# salary1 = int(input("What is your yearly salary? (just enter numbers with no punctuation) $"))
# job_length1 = float(input("How many months have you been in your job? Do not round up your answer. So if it's been 2 years, 3 months and 20 days, please write '27' months."))

# if (salary1 > 49999):
#     (job_length1 >= 36)
#     print("Congratulations, you are eligible for a loan")
# else:
#     print("Apologies, but you are not eligible for a loan")

# num00 = int(input("Please input a number: "))

# if (num00==10):
#     print("ten")
# elif (num00==11):
#     print("eleven")
# elif (num00==12):
#     print("twelve")
# else:
#     print(" the number is unknown")

# name1 = str(input("What is your name? "))
# if (name1=="Frank" or "frank"):
#     print("Greetings")
# else:
#     print("Sorry, we do not greet people with that name.")

from datetime import date
now = date.today()
print("The year is:", now.year)
DOB = int(input("What is your Year of birth: "))
print("This year you turn ",(now.year-DOB),"Years old")
print("Come in and have a drink after your birthday!")

# password = "Rela238#"
# userPassword = input("Please enter your password: ")
# if (password == userPassword):
#     print("Password accepted and intercepted")
# else:
#     print("The password is incorrect")

# score = int(input("What is your score out of 100? "))
# A_score = 90
# B_score = 80
# C_score = 70
# D_score = 60

# if (score >= A_score):
#     print("your grade is A")
# else:
#     if (score >= B_score):
#         print("your grade is B")
#     else:
#         if (score >= C_score):
#              print("your grade is C")
#         else:
#             if (score >= D_score):
#                 print("your grade is D")
#             else:
#                 print("your grade is F which unfortunately means Fail")

# grade = int(input("What was your grade? "))
# if (grade >= 90 and grade < 101):
#     print("Your grade is a High Distinction")
# else:
#     if (grade >= 80 and grade < 90):
#         print("Your grade is a Distinction")
#     else:
#         if (grade >= 70 and grade < 80):
#             print("Your grade is a Credit")
#         else:
#             if (grade >= 60 and grade < 70):
#                 print("Your grade is a Pass")
#             else:
#                 if (grade >= 0 and grade < 60):
#                     print("Your grade fell below our requirements.")
#                 else:
#                     if (grade > 100):
#                         print("You have inputted a number outside the possibilities for this class.")